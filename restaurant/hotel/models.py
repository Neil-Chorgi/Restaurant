from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits = 12,decimal_places = 2,default = 0)