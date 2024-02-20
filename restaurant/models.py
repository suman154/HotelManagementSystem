from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200)


class Food(models.Model):
    nmae = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu,on_delete=models.SET_NULL,null=True)



