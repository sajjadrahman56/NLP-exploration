from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #  object of Chrome WebDriver 
driver.maximize_window()

root_path ='https://www.daraz.com.bd/products/cudy-wr1300-ac1200-867mbps-5ghz-300mbps-at-24ghz-5x-4-x-5dbi-i276529930-s1255947350.html'



driver.get(root_path)

time.sleep(30)

height = driver.execute_script('return document.body.scrollHeight')

for i in range(0,height+1000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)
print(height)
driver.quit()
