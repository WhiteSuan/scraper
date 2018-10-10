from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,WebDriverException
import sys

browser = webdriver.Chrome()
browser.get("https://www.adairs.com.au/furniture/bedheads/")
delay = 10 # seconds 
try:
	myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME,"lazy")))
	html = browser.page_source
	browser.close()
	print(html)
except TimeoutException:
	print ("Loading took too much time!")
	browser.close()
except WebDriverException as e:
	print(str(e))
	browser.close()