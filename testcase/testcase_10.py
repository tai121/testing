from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv
import logging
import re
import random

load_dotenv()
logging.basicConfig(filename='./logs/testcase_10.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
action = ActionChains(driver)
website_url = "http://teststore.automationtesting.co.uk"
size = None
type = None

def float_value(s):
    return float(s[1:])


def visit_website():
    driver.get(website_url)


def check_quickview():
    product_element = driver.find_elements(By.CLASS_NAME,"product-thumbnail")
    number = random.randint(0,len(product_element)-1)

    number = 0


    chosend_element = product_element[number]
    action.move_to_element(chosend_element).perform()
    # time.sleep(1000)
    quick_view = driver.find_element(By.CSS_SELECTOR,'a.quick-view')
    
    try:
        quick_view.click()
    except:
        logging.error("Test fail: Quickview didn't open")
    
    time.sleep(3)
    modal = driver.find_elements(By.CLASS_NAME,'modal-dialog-centered')
    if len(modal) == 0:
        logging.error("Test fail: Quickview didn't open")
        return
    logging.info("Test pass: Quickview work")
    input_color = driver.find_elements(By.CLASS_NAME,"input-color")
    
    
    if len(input_color)!=0:
        number = random.randint(0,len(input_color)-1)
        input_color[number].click()

        chosen = driver.find_element(By.CSS_SELECTOR,'span.color span.sr-only')
        type = chosen.text

    selector = driver.find_elements(By.TAG_NAME,"select")
    if len(selector)==0:
        return
    

    selector[0].click()
    time.sleep(3)
    option_sizes = driver.find_elements(By.TAG_NAME,"option")   
    number = random.randint(0,len(option_sizes)-1)
    size = option_sizes[number].text

    option_sizes[number].click()


    button = driver.find_element(By.CLASS_NAME,'close')
    errors = driver.find_elements(By.CLASS_NAME,'ajax-error')
    

def check_cart():

    cart_button = driver.find_element(By.CSS_SELECTOR,'div.product-quantity div.add button.add-to-cart')
    
    cart_button.click()
    time.sleep(7)
    try:
        cart = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CSS_SELECTOR,"h4.modal-title")))
        if 'Product successfully added to your shopping cart' in cart.
    except:
        print("lor r")    
    elements = driver.find_elements(By.CSS_SELECTOR,'div.row div.col-md-6 span strong')
    print(len(elements))

def testcase_10():
    visit_website()
    check_quickview()
    check_cart()
    
    
    
    

    

if __name__ == "__main__":
    testcase_10()