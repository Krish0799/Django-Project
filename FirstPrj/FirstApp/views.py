from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestMeth(request):
	msg = '<h1> Test Success </h1>'
	return HttpResponse(msg) 
