from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
import requests

def home(request):
	return render(request,'index.html')
def news(request):
	a3 = "&apiKey=" + "dcf42dec7d614e778d3dcd8616ab8182"
	wa = "https://newsapi.org/v2/top-headlines?country=in&category=business"+a3
	res = requests.get(wa)
	data = res.json()
	news = data['articles']
	return render(request,'news.html',{'news':news})
def ulogout(request):
	logout(request)
	return render(request,'index.html')
	