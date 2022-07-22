from selenium import webdriver # pip install selenium
from selenium.webdriver.common.keys import Keys # pip install webdriver_manager
import time
import random
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())


chrome.get("https://web.whatsapp.com")

time.sleep(30)

search_box = chrome.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
search_box.send_keys("Swapnoneel Kayal")
search_box.send_keys(Keys.ENTER)

time.sleep(3)


for i in range(0,500):
    message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    message_box.send_keys("Moo mein lelo pls apna")
    message_box.send_keys(Keys.ENTER)

message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
message_box.send_keys("Enjoy The Spam!!!!!")
message_box.send_keys(Keys.ENTER)

#emoji = [':-)', ':-(', '>_<', ';-)']

#for i in range(0,1000):
    #message_box = chrome.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    #message_box.send_keys(random.choice(emoji))
    #message_box.send_keys(Keys.ENTER)
