from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #  object of Chrome WebDriver class to control the browser

root_path ='https://newsroom.pinterest.com/company/'

driver.get(root_path) # get = open the URL in the browser ||  data pass through the url when we use get method

driver.maximize_window() # maximize the window

link = driver.find_element(By.XPATH,'/html/body/main/section[2]/div/div/div/div/div/div[1]/div')
print('I am inside now  ---------------------------------------')
print()
print(link.get_attribute('href')) # get the value of the href attribute of the link
driver.get(link.get_attribute('href')) # open the link in the browser
time.sleep(100)