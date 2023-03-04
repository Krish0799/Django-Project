from django.shortcuts import render
from django.http import HttpResponse
import datetime
#Greetigs app view
# Create your views here.

def GreetWithTime(respones):
	time = datetime.datetime.now()
	#.today() to display todays date
	msg = '<h1> Hi ,Time is '+str(time)+'</h1>'
	return HttpResponse(msg)
