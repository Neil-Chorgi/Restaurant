from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Dish,Order
from django.views.generic.edit import DeleteView
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

def order_page(request):
    order_list = Order.objects.all()
    template = loader.get_template('hotel/order.html')
    context = {'order_list': order_list,
    }
    #o = "Dish:",order_list.order_dish,"Quantity",str(order_list.quantity),"Extra notes:",order_list.extra_notes
    return HttpResponse(template.render(context, request))

def delete(request,order_id):
    order_list = Order.objects.all()
    order_place = int(order_id-4)
    '''
    template = loader.get_template('hotel/confirm_delete.html')
    context = {'object': order_list[order_place],
    }
    return HttpResponse(template.render(context, request))
    '''
    o = Order.objects.get(id = order_id)
    o.delete()
    
    return HttpResponse("Deleted")