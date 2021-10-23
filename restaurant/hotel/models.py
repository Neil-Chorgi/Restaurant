from django.db import models

# Create your models here.
class Dish(models.Model):
    dish_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length = 200)
    price = models.DecimalField(default=0)