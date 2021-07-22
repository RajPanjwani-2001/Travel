from django.db import models 
'''
# Create your models here.
class Destination :
    id : int
    name : str
    image : str
    desc : str
    price : int
    offer : bool
'''
#if you want to convert class into model then,
class Destination(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField() 
    price = models.IntegerField()
    offer = models.BooleanField(default=False)