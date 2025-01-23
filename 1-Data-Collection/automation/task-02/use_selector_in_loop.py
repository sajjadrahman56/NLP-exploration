# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome() #  object of Chrome WebDriver 

# root_path ='https://newsroom.pinterest.com/impact/'

# driver.get(root_path) # get = open the URL in the browser ||  data pass through the get

# driver.maximize_window() # maximize the window

# link_list = []
# for i in range(1,11):
#     type_i = str(i)
#     link = driver.find_element(By.CSS_SELECTOR, '#\\37GTE28Q1BkZQDPxvUhAh2p > div.BusinessDirectoryGrid.BusinessDirectoryGrid__blog > div:nth-child('+type_i+') > div > div > a').get_attribute('href')
#     # link = driver.find_element(By.XPATH,'//*[@id="7GTE28Q1BkZQDPxvUhAh2p"]/div[3]/div['+type_i+']/div/div/a').get_attribute('href')
                                         
#     link_list.append(link)


# print(len(link_list))

# time.sleep(100)

# driver.quit()



# # //*[@id="7GTE28Q1BkZQDPxvUhAh2p"]/div[3]/div[1]/div/div/a  
# # //*[@id="7GTE28Q1BkZQDPxvUhAh2p"]/div[3]/div[2]/div/div/a  

# # //*[@id="7GTE28Q1BkZQDPxvUhAh2p"]/div[3]/div[20]/div/div/a

# #\37 GTE28Q1BkZQDPxvUhAh2p > div.BusinessDirectoryGrid.BusinessDirectoryGrid__blog > div:nth-child(1)> div > div > a
# #\37 GTE28Q1BkZQDPxvUhAh2p > div.BusinessDirectoryGrid.BusinessDirectoryGrid__blog > div:nth-child(2) > div > div > a
# #\37 GTE28Q1BkZQDPxvUhAh2p > div.BusinessDirectoryGrid.BusinessDirectoryGrid__blog > div:nth-child(20)> div > div > a


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

root_path = 'https://newsroom.pinterest.com/impact/'
driver.get(root_path)
driver.maximize_window()

link_list = []

# Wait for the main container to load
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#\\37GTE28Q1BkZQDPxvUhAh2p'))
)

# Get all child elements in the blog grid
elements = driver.find_elements(By.CSS_SELECTOR, '#\\37GTE28Q1BkZQDPxvUhAh2p > div.BusinessDirectoryGrid.BusinessDirectoryGrid__blog > div')

for element in elements:
    try:
        # Find the link inside each child element
        link = element.find_element(By.CSS_SELECTOR, 'div > div > a').get_attribute('href')
        link_list.append(link)
    except Exception as e:
        print(f"Error: {e}")

print(f"Number of links found: {len(link_list)}")
print(link_list)

time.sleep(10)
driver.quit()
