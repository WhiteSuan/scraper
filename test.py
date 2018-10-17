from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from w3lib.http import basic_auth_header
import sys

proxy = "proxy.crawlera.com:8010"
username = "fcb973633f45443cb0999a782ac6f286"
password = ""

service_args = [
	"--ignore-ssl-errors=true",
	"--ssl-protocol=any",
	"--proxy={}".format(proxy),
	"--proxy-type=http",
]

caps = DesiredCapabilities.PHANTOMJS
authentication_token = basic_auth_header(username, password).decode('utf-8')
caps['phantomjs.page.customHeaders.Proxy-Authorization'] = authentication_token

driver = webdriver.PhantomJS(
	service_args=service_args,
	desired_capabilities=caps
)
driver.get("https://www.empiretoday.com/")
html = driver.page_source
driver.close()
print(html)