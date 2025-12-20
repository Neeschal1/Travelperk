from django.db import models
from apps.packages.models.choices import *

class Packages(models.Model):
    Package_Provider = models.CharField(max_length=30)
    Continent = models.CharField(max_length=15, choices=CONTINENTS_CHOICE)
    Trip_Difficulty = models.CharField(max_length=15, choices=TRIP_DIFFICULTY)
    Type = models.CharField(max_length=15, choices=TRAVEL_TYPE)
    Trip_Category = models.CharField(max_length=15, choices=TRIP_CATEGORY)
    Accomodation = models.CharField(max_length=20, choices=ACCOMMODATION_TYPE)
    Highlights = models.TextField()
    Total_Estimated_Cost = models.IntegerField()
    Total_Estimated_Duration = models.CharField()
    
    def __str__(self):
        return self.Package_Provider