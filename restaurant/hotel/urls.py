from django.urls import path

from . import views

urlpatterns = [
    #path('',views.homepage, name = 'homepage'),
    path('', views.index, name='index'),
    #if the path is ' ' then run function name 'index'
    path('<int:dish_id>/',views.menu, name = 'menu'),
    
    path('order/', views.order_page,name = 'order_page'),
    
    path('order/<int:order_id>/',views.delete,name = 'delete'),
]
