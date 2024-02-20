from django.db import models
from management.models import Room

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField()


class CustomerRoom(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    room = models.ForeignKey(Room,on_delete=models.SET_NULL,null=True )