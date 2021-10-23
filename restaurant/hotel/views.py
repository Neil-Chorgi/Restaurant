from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #runs if url = ' ' 
    return HttpResponse("You are at the Restaurant.")