
from selenium import webdriver
from selenium.webdriver.common.keys import Keys   #for necessary browser action
import time #used for sleep function
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def interface():

    def Ok():
        uname = e1.get()
        password = e2.get()

        if(uname != "" and password != "") :
            automatic(uname,password,current_value1.get(),current_value3.get(),current_value.get())

        else :
            
            messagebox.showinfo("", "Blank Not allowed")

    global root
    root = tk.Tk()
    root.title("Login")
    root.geometry("600x200")
    global e1
    global e2

    Label(root, text="Email").place(x=10, y=10)
    Label(root, text="Password").place(x=10, y=40)
    Label(root, text="Ads renew timer").place(x=10, y=70)
    Label(root, text="Number of Ads").place(x=10, y=100)
    Label(root, text="Seconds").place(x=250, y=68)
    Label(root, text="Minutes").place(x=400, y=68)

    e1 = Entry(root,width=50)
    e1.place(x=200, y=10)

    e2 = Entry(root,width=50)
    e2.place(x=200, y=40)
    e2.config(show="*")
    current_value = tk.StringVar(value=1)
    current_value1 = tk.StringVar(value=1)
    current_value3 = tk.StringVar(value=0)
    


    c1 = tk.Spinbox(
    root,
    from_=1,
    to=60,
    width=5,
    textvariable=current_value1,
    wrap=True).place(x=200,y=70)
    c3 = tk.Spinbox(
    root,
    from_=0,
    to=100,
    width=5,
    textvariable=current_value3,
    wrap=True).place(x=350,y=70)

    spin_box = tk.Spinbox(
    root,
    from_=1,
    to=100,
    textvariable=current_value,
    wrap=True)

    spin_box.place(x=200,y=100)






    Button(root, text="Login", command=Ok ,height = 2, width = 13).place(x=270, y=140)

    root.mainloop()


def automatic(uname,password,seconds,minutes,nbrAds):
    driver = webdriver.Firefox()
    driver.get(f"https://www.milanuncios.com/mis-anuncios/")
    c=0
    try:
        

        
        cookies=driver.find_element_by_xpath('//*[@data-testid="TcfAccept"]')
        if  cookies is not None:
            ActionChains(driver).move_to_element(cookies).click().perform()
        time.sleep(5)
        email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email.send_keys(uname)
        element = driver.find_element_by_xpath('//*[@id="password"]')
        element.send_keys(password)

        element =driver.find_element_by_xpath('//*[@class="sui-AtomButton sui-AtomButton--primary sui-AtomButton--solid sui-AtomButton--center sui-AtomButton--fullWidth ma-FormLogin-submitButton"]')
        ActionChains(driver).move_to_element(element).click().perform()

        #element.send_keys("mohammedbusben@gmail.com")
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="ma-UserAvatar"]')))
        driver.get(f"https://www.milanuncios.com/mis-anuncios/")
        time.sleep(3)
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,'//*[@for="description-inline2"]')))
        string1 = str("javascript:document.getElementById('description-inline2').click();")
        driver.execute_script(string1)
        time.sleep(3)
        element=WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH,'//*[@class="ma-ButtonBasic ma-ButtonBasic--primary ma-ButtonBasic--medium ma-ButtonBasic--fullWidth"]')))
        ActionChains(driver).move_to_element(element).click().perform()


        driver.refresh()
        element=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@data-e2e="ma-AdCard-titleLink"]')))
        btn = driver.find_elements_by_css_selector('.ma-NavigationPagination-pagesContainer button')

        print(len(btn))
        for i in range(int(len(btn)/2)):
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@data-e2e="ma-AdCard-titleLink"]')))
            
            next= btn[i]
            ActionChains(driver).move_to_element(next).click().perform()
            time.sleep(5)
            for i in range(25):
                driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

            button = driver.find_elements_by_css_selector('.ma-AdCard footer .ma-AdButtonBarMyAds li:nth-child(2) button ')
            times = driver.find_elements_by_css_selector(".ma-AdCard-time--header time")
            end=0
            
            for x in range(0,len(button)):
                txt =str(times[x].text)
                #if int(t)==1:
                if "días" in txt:
                    button[x].click()
                    c+=1
                    if c==int(nbrAds):
                        end =1
                        time.sleep(3)
                        break
                    else:
                        time.sleep(int(seconds)+60*int(minutes))

                elif "horas" in txt:
                    if int(txt[:2])>=15:
                        button[x].click()
                        c+=1
                        if c==int(nbrAds):
                            end =1
                            time.sleep(3)
                            break
                        else:
                            time.sleep(int(seconds)+60*int(minutes))
                """ else:
                    if "días" in txt:
                        button[x].click()
                        c+=1
                        if c==int(nbrAds):
                                end =1
                                break
                    elif "horas" in txt:
                        if int(txt[:2])>=15:
                            button[x].click()
                            c+=1
                            if c==int(nbrAds):
                                end =1
                                break"""
            if end ==1:
                break
                        
            driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
            time.sleep(2)

    except Exception as e :
        print(e)
    driver.close()
    messagebox.showinfo("", "Automatization Done !")
    root.destroy()

if __name__ == '__main__':
    interface()