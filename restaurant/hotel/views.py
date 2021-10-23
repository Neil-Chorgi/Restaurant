from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dish
# Create your views here.

def index(request):
    #runs if url = ' ' 
    return HttpResponse("You are at the Restaurant.")

def menu(request, dish_id):
    #return HttpResponse("You're looking at dish %s." % dish_id)
    menu_list = Dish.objects.all()
    
    d = menu_list[dish_id]
    output = d.dish_text+", "+d.description_text+". Price: £"+str(d.price)
    return HttpResponse(output)