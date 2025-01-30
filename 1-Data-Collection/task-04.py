from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# chrome_options = Options()
# chrome_options.add_argument("--disable-cache")
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

driver.maximize_window()

root_path ='https://www.daraz.com.bd/products/tp-link-tl-wr820n-v2-300-mbps-multi-mode-wi-fi-router-i133488288.html?'


driver.get(root_path)

time.sleep(30)

height = driver.execute_script('return document.body.scrollHeight')

for i in range(0,height+1000,30):
    driver.execute_script(f'window.scrollTo(0,{i});')
    time.sleep(0.5)

product_information = {}
product_information['product_name'] = driver.find_element(By.CSS_SELECTOR, '#module_product_title_1 > div > div > h1').text
product_information['total_review'] = driver.find_element(By.CSS_SELECTOR, '#module_product_review_star_1 > div > a:nth-child(2)').text
product_information['brand_name'] = driver.find_element(By.CSS_SELECTOR, '#module_product_brand_1 > div > a.pdp-link.pdp-link_size_s.pdp-link_theme_blue.pdp-product-brand__brand-link').text
product_information['price'] = driver.find_element(By.CSS_SELECTOR, '#module_product_price_1 > div > div > span').text

product_information['details'] = driver.find_element(By.CSS_SELECTOR, '#module_product_detail > div > h2').text


details_list = []
container = driver.find_element(By.CSS_SELECTOR, '#module_product_detail > div > div > div.pdp-product-desc.height-limit > div.html-content.pdp-product-highlights > ul')

list_items = container.find_elements(By.TAG_NAME, 'li')

details_list = []

for idx, item in enumerate(list_items, 1):
    details_list.append(f"{idx}. {item.text}")
product_information['details_list'] = details_list

print(height)
print('----------------------------')
print(product_information)
driver.quit()
