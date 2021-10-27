from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Dish(models.Model):
    #Variables
    DISH_TYPE = (
        ('STARTER', "Starter"),
        ('MAIN', "Main dish"),
        ('DESSERT', "Dessert"),
        ('DRINK',"Drink"),
        
    )
    dish_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length = 1000)
    price = models.DecimalField(max_digits = 12,decimal_places = 2,default = 0,validators=[MaxValueValidator(100),MinValueValidator(1)],)
    type_of_dish = models.CharField(max_length = 50,choices = DISH_TYPE,default = 'MAIN',)
    
    def __str__(self):
        return self.dish_text

class Order(models.Model):
    order_dish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    extra_notes = models.CharField(max_length = 1000, default = "None")
    def __str__(self):    
        return 'Dish: {}, quantity: {}, extra notes: {}'.format(self.order_dish, self.quantity, self.extra_notes)
    