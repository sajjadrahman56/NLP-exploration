from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #  object of Chrome WebDriver class to control the browser

root_path ='https://newsroom.pinterest.com/company/'

driver.get(root_path) # get = open the URL in the browser ||  data pass through the

driver.maximize_window() # maximize the window

link = driver.find_element(By.CSS_SELECTOR,'#__PWS_ROOT__ > div > div > div > div > div:nth-child(4) > div > div > div > div.BusinessRelatedArticles.BusinessRelatedArticlesEDHub.BusinessRelatedArticlesNoCarousel > div.BusinessDirectoryGrid.BusinessDirectoryGrid_centered.BusinessDirectoryGrid_stretch.BusinessDirectoryGrid__EDHub > div:nth-child(2) > div > div > a')

print(link.get_attribute('href')) # get the value of the href attribute of the link

driver.get(link.get_attribute('href')) # open the link in the browser

time.sleep(30)

driver.quit()



# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome() #  object of Chrome WebDriver class to control the browser

# root_path ='https://newsroom.pinterest.com/company/'

# driver.get(root_path) # get = open the URL in the browser ||  data pass through the

# driver.maximize_window() # maximize the window

# link = driver.find_element(By.XPATH,'//*[@id="__PWS_ROOT__"]/div/div/div/div/div[4]/div/div/div/div[5]/div[2]/div[1]/div/div/a')

# print(link.get_attribute('href')) # get the value of the href attribute of the link

# driver.get(link.get_attribute('href')) # open the link in the browser

# time.sleep(30)

# driver.quit()