from django.db import models

# Create your models here.
class Food(models.Model):
    food_item = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
