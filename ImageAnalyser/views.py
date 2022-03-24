from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def viewImage(request):
	return HttpResponse("You Discovered an Unreleased Feature")