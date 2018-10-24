from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys

browser = webdriver.Chrome(executable_path=r"C:\Users\ynxnguyen\Downloads\chromedriver_win32\chromedriver.exe")
browser.get("https://www.bedbathandbeyond.com/store/category/gifts/gifts-by-interest/fitness-health-gifts/14830?ml=v2&icid=gift_promo17")
delay = 10 # seconds
try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'prodImg')))
    html = browser.page_source
    browser.close()
    print(html)
except TimeoutException:
    print ("Loading took too much time!")
    browser.close()
