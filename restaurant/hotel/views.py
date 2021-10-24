from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dish
# Create your views here.

def index(request):
    '''
    #runs if url = ' ' 
    return HttpResponse("You are at the Restaurant.")
    '''
    menu_list = Dish.objects.all()
    template = loader.get_template('hotel/index.html')
    context = {
        'menu_list': menu_list,
    }
    return HttpResponse(template.render(context, request))
    
    
def menu(request, dish_id):
    #return HttpResponse("You're looking at dish %s." % dish_id)
    menu_list = Dish.objects.all()
    
    d = menu_list[dish_id - 1]
    output = d.dish_text+", "+d.description_text+". Price: £"+str(d.price)
    return HttpResponse(output)
'''
def homepage(request):
    context = {'foo':'bar'}
    return render(request, 'templates/hotel/homepage.html', context) 
'''