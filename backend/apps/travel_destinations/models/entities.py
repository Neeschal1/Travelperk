from django.db import models
from django.contrib.auth.models import User
from .choices import *

class Desired_Travel_Destination(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True)
    Dream_Continent = models.CharField(max_length=15, choices=CONTINENTS_CHOICE)
    Trip_Difficulty = models.CharField(max_length=15, choices=TRIP_DIFFICULTY)
    Interest = models.CharField(max_length=15, choices=TRAVEL_INTERESTS)
    Trip_Category = models.CharField(max_length=15, choices=TRIP_CATEGORY)
    Accomodation = models.CharField(max_length=20, choices=ACCOMMODATION_TYPE)
    
    def __str__(self):
        return self.Dream_Continent