from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link_dict = {}

for page in range(1, 11):
    driver.get(f'https://www.daraz.com.bd/routers/?page={page}')  
    driver.maximize_window() 

    links_for_page = []  
    for product in range(1, 41):   
            link = driver.find_element(By.CSS_SELECTOR, '#root > div > div.ant-row.FrEdP.css-1bkhbmc.app > div:nth-child(1) > div > div.ant-col.ant-col-20.ant-col-push-4.Jv5R8.css-1bkhbmc.app > div._17mcb > div:nth-child('+str(product)+') > div > div > div.buTCk > div.RfADt > a').get_attribute('href')
            links_for_page.append(link)

    link_dict[f"page_{page}"] = links_for_page

print(link_dict)
time.sleep(30)
driver.quit()
