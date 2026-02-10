from django.db import models
from django.contrib.auth.models import User
from .choices import *

class Car(models.Model):
    Car_Name = models.CharField(max_length=30, default='Ford')
    Car_Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Car_Model = models.CharField(max_length=50, default='Mustang')
    Car_Seats = models.IntegerField(default=5)
    Car_Color = models.CharField(max_length=10, choices=CAR_COLOR_CHOICE, default='Black')
    
    def __str__(self):
        return self.Car_Name