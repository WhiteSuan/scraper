"""javascriptscrape URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from .views import APIview, API, PROXYview, PROXY

urlpatterns = [
	path('', APIview.as_view(), name='api'),
	path('getHtml', API.as_view(), name='api'),
	path('proxy', PROXYview.as_view(), name='api'),
	path('getProxy', PROXY.as_view(), name='api'),
]