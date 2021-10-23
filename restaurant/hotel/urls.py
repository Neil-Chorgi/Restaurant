from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #if the path is ' ' then run function name 'index'
    path('<int:dish_id>/',views.menu, name = 'menu'),
]