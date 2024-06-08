from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<center><h2>welcome to my My restorent</h2></center>')
