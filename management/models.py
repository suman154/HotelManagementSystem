from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email  = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['useraname']


class RoomType(models.Model):
    name = models.CharField(max_length=255)


class Room(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.ForeignKey(RoomType, on_delete=models.SET_NULL,null=True)
    floor = models.CharField(max_length=255)
    status = models.CharField(max_length=255)




