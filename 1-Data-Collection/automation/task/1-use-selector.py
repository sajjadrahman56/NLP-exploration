from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

root_path ='https://www.daraz.com.bd/routers/'

driver.get(root_path)
driver.maximize_window() 

link = driver.find_element(By.CSS_SELECTOR,'#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child(4) > div > div > div.buTCk > div.RfADt > a')

print(link.get_attribute('href'))  

driver.get(link.get_attribute('href')) 

time.sleep(30)

driver.quit()