from django.shortcuts import render,HttpResponse
import requests

def index(Request):
	data = True
	result = None
	globalSummary = None
	countries = None
	while (data):
		try:
			result = requests.get('https://api.covid19api.com/summary')
			json = result.json()
			globalSummary = json['Global']
			countries = json['Countries']
			data = False
		except:
			data = True
	return render(Request,'index.html',{'globalSummary':globalSummary,'countries':countries})


def index1(Request):
	data = True
	result = None
	country = None
	while (data):
		try:
			result = request.get('https://api.covid19api.com/total/dayone/country/India')
			json = result.json()
			country = json['Country']
			data = False
		except:
			data=True
	return render(Request,'index1.html',{'country':Country})
