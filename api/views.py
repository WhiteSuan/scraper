from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from django.http import JsonResponse

# Create your views here.
def jsscraper(var1,var2,var3):
	browser = webdriver.Chrome(executable_path=r"C:\Users\ynxnguyen\Downloads\chromedriver_win32\chromedriver.exe")
	browser.get(var1)
	delay = 100 # seconds 
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
		