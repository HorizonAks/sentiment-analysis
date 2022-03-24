from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def viewhome(request):
	template = loader.get_template('home/homepage.html')
	return HttpResponse(template.render({},request))