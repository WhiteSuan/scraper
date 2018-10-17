from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from w3lib.http import basic_auth_header
from django.http import JsonResponse



# Create your views here.
def jsscraper(var1,var2,var3):
	options = Options()
	options.add_argument("start-maximized");
	options.add_argument("disable-infobars");
	options.add_argument("--disable-extensions");
	options.add_argument("--disable-gpu");
	options.add_argument("--disable-dev-shm-usage");
	options.add_argument("--no-sandbox");
	browser = webdriver.Chrome(chrome_options=options)
	browser.get(var1)
	delay = 10 # seconds
	try:
		if (var2 == "class"):
			myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME, var3)))
		elif (var2 == "id"):
			myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, var3)))
		html = browser.page_source
		browser.close()
		print(html)
		return HttpResponse(html)
	except TimeoutException:
		return HttpResponse("Loading took too much time!")
		browser.close()

def proxyscraper(var4):
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
	driver.get(var4)
	html = driver.page_source
	driver.close()
	print(html)
	return HttpResponse(html)

class APIview(TemplateView):
	template_name = 'api/test.html'
	def get(self,request):
		if request.method == "GET" and '1' in request.GET:
			var1 = request.GET.get("url")
			var2 = request.GET.get("type")
			var3 = request.GET.get("selector")
			print(var1, var2, var3)
			return jsscraper(var1,var2,var3)
		else:
			return render(request, self.template_name)
		
class API(TemplateView):
	template_name = 'api/test.html'			
	def get(self,request):
		var1 = request.GET.get("url")
		var2 = request.GET.get("type")
		var3 = request.GET.get("selector")
		print(var1, var2, var3)
		return jsscraper(var1,var2,var3)

class PROXYview(TemplateView):
	template_name = 'api/proxy.html'
	def get(self,request):
		if request.method == "GET" and '1' in request.GET:
			var4 = request.GET.get("link")
			return proxyscraper(var4)
		else:
			return render(request, self.template_name)

class PROXY(TemplateView):
	template_name = 'api/proxy.html'
	def get(self,request):
		var4 = request.GET.get("link")
		return proxyscraper(var4)