from django.db import models
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
    price = models.DecimalField(max_digits = 12,decimal_places = 2,default = 0)
    type_of_dish = models.CharField(max_length = 50,choices = DISH_TYPE,default = 'MAIN')
    
    def __str__(self):
        return self.dish_text