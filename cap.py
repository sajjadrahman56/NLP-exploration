import time
import undetected_chromedriver as uc
import pytesseract
import cv2
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup ChromeDriver
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the undetected driver
driver = uc.Chrome(options=options)

# Open the target website (Change the URL to the CAPTCHA page)
driver.get("https://www.google.com/")

# Wait for CAPTCHA to load and refresh the page
time.sleep(3)
driver.refresh()

# Perform search
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("bal and sal video")
search_box.send_keys(Keys.RETURN)
time.sleep(10)

# Wait for the reCAPTCHA checkbox to be visible
try:
    recaptcha_checkbox = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "g-recaptcha"))
    )
    
    # Use ActionChains to click the reCAPTCHA checkbox
    action = ActionChains(driver)
    action.move_to_element(recaptcha_checkbox).click().perform()

    time.sleep(10)  # Wait for CAPTCHA to be solved or challenge to load

except Exception as e:
    print("Error finding reCAPTCHA:", e)

# Navigate to Google Maps after CAPTCHA
# g_map = driver.find_element(By.XPATH,'//*[@id="hdtb-sc"]/div/div/div[1]/div/div[2]/a').click()
time.sleep(5)

# If a CAPTCHA image appears (not reCAPTCHA), solve it
try:
    captcha_image = driver.find_element(By.XPATH, "//img[@id='captcha_image']")  # Update as needed
    captcha_image.screenshot("captcha.png")

    # Load the image and convert it to grayscale
    image = cv2.imread("captcha.png")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract OCR to extract text
    captcha_text = pytesseract.image_to_string(gray).strip()
    print("Extracted CAPTCHA:", captcha_text)

    # Locate CAPTCHA input field and enter the extracted text
    captcha_input = driver.find_element(By.XPATH, "//input[@id='captcha_input']")  # Update as needed
    captcha_input.send_keys(captcha_text)

    # Submit the form (Modify this based on your website)
    captcha_input.send_keys(Keys.RETURN)

except Exception as e:
    print("No CAPTCHA image found or solved:", e)

# Wait and close the driver
time.sleep(5)
driver.quit()
