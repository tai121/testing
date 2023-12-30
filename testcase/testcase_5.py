from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import logging
import re

load_dotenv()
logging.basicConfig(filename='./logs/testcase_5.log',level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = webdriver.Chrome()
website_url = "http://teststore.automationtesting.co.uk/6-accessories"



def visit_website():
    driver.get(website_url)

def get_total_product():
    total_element = driver.find_element(By.CSS_SELECTOR,"div.total-products p")
    matches = re.findall(r'\d+', total_element.text)

    if matches:
        return int(matches[0])


def verify_number_of_product(total):
    list_product=driver.find_elements(By.CSS_SELECTOR,"article.product-miniature")
    if total == len(list_product):
        logging.info(f"Test pass: The page already displays all products")
    else:
        logging.error(f"Test fail: The number of products displayed is incorrect")

def testcase_5():
    visit_website()
    
    verify_number_of_product(get_total_product())

if __name__ == "__main__":
    testcase_5()