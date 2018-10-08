from django.test import TestCase

# Create your tests here.
from selenium import webdriver
from django.http import HttpResponse
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys

def jsscraper(request):
	browser = webdriver.Chrome(executable_path=r"C:\Users\ynxnguyen\Downloads\chromedriver_win32\chromedriver.exe")
	browser.get("https://www.adairs.com.au/furniture/bedheads/")
	delay = 15 # seconds 
	try:
		myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "lazy")))
		html = browser.page_source
		browser.close()
		return HttpResponse(html)
	except TimeoutException:
		return HttpResponse("Loading took too much time!")
		browser.close()