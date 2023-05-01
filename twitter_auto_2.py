from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from time import sleep

email = 'ananyabaghel2004@gmail.com'
password = "asdfghjk1234"
username = 'AnanyaB106'

def wait(driver, xpath, t = 10):
    try:
        element = WebDriverWait(driver, t).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
    except:
        pass

try:
    driver = webdriver.Chrome('/Users/anna/Downloads/chromedriver_mac64/chromedriver.exe')
    driver.get("https://www.twitter.com/login")


    nextBP = '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]'
    wait(driver, nextBP)
    uname = driver.find_elements('xpath', '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')[0]
    uname.send_keys(email)
    nextB = driver.find_elements('xpath', nextBP)[0]
    nextB.click()

    loginBt = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div'
    wait(driver, loginBt)
    sleep(0.2)

    unusual_pth = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'

    if EC.presence_of_element_located((By.XPATH, unusual_pth)):
        unusual = driver.find_elements('xpath', unusual_pth)[0]
        unusual.click()
        unusual.send_keys(username)
        sleep(0.2)
        login = driver.find_elements('xpath', loginBt)[0]
        login.click()
        sleep(0.2)
        wait(driver, loginBt)


    sleep(1)
    pswd = driver.find_elements('xpath', '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')[0]
    pswd.click()
    pswd.send_keys(password)
    sleep(0.2)
    login = driver.find_elements('xpath', loginBt)[0]
    login.click()

    driver.get('https://twitter.com/elonmusk')
    
    n = int(input())
    #n = 7

    sleep(3)

    for i in range(n*2):
        driver.execute_script("window.scrollTo(0,4000)")
        sleep(1)

    htmlcode=(driver.page_source).encode('utf-8')
    soup = BeautifulSoup(htmlcode,features="html.parser")

    s = []
    x=soup.findAll(['div'] , class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    for i in x:
        try:
            s.append(i.get_text())
        except:
            pass
    pn = len(s) if len(s)<n else n
    print(pn)
    print('_____')
    for i in range(pn):
        print(s[i])
        print('---------------------------------------------')


except Exception as e:
    print(e)

input()