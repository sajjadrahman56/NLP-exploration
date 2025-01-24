from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set Chrome options

driver = webdriver.Chrome() #  object of Chrome WebDriver class to control the browser

driver.get('https://www.daraz.com.bd/routers/') 
driver.maximize_window() 

link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[4]/div/div/div[1]/div/a')


print(link.get_attribute('href')) # get the value of the href attribute of the link

driver.get(link.get_attribute('href')) # open the link in the browser

 
time.sleep(100)


driver.quit() # close the browser
# query param -> amra kuno kichu patai jeta theke amra kuno kichu pai nah 
# TODO: query param niya work korte hobe 