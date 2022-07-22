from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import random
from getpass import getpass

chrome = webdriver.Chrome(ChromeDriverManager().install())

chrome.get("https://www.instagram.com")

time.sleep(2)
username = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("username")

password = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("password")
login_button = chrome.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()

#time.sleep(3)
#veri_code = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[1]/div/label/input')
#veri_code.send_keys("otp")
#veri_code.send_keys(Keys.ENTER)

time.sleep(5)
save_info = chrome.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
save_info.click()

time.sleep(1)
notif = chrome.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notif.click()

search_bar = chrome.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_bar.send_keys('shweta.varshney')
time.sleep(2)
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)

time.sleep(5)
like = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
like.click()

time.sleep(1)
next_btn = chrome.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a') #first post has only next button, no previous buttom hence it ends with /a
next_btn.click()

time.sleep(3)

while True:

    try:
      like = chrome.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
      like.click()

      next_btn = chrome.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]') #first post has only next button, no previous buttom hence it ends with /a
      next_btn.click()
      time.sleep(5)


    except:
        close_btn = chrome.find_element_by_xpath('/html/body/div[5]/div[3]/button/div/svg')
        close_btn.click()
        break
