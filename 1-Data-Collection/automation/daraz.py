from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #  object of Chrome WebDriver class to control the browser 

driver.get('https://www.daraz.com.bd') # get = open the URL in the browser ||  data pass through the url when we use get method

driver.maximize_window() # maximize the window 
time.sleep(100)
driver.quit() # close the browser
# query param -> amra kuno kichu patai jeta theke amra kuno kichu pai nah 
# TODO: query param niya work korte hobe 