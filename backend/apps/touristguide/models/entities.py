from django.db import models
from apps.touristguide.models.choices import *

class Touristguide(models.Model):
    Tourist_Guide_Name = models.CharField(max_length=70)
    Tourist_Guide_Address = models.CharField(max_length=100)
    Tourist_Guide_Age = models.IntegerField(default=25)
    Tourist_Guide_Sex = models.CharField(max_length=6, choices=TOURIST_GUIDE_SEX)
    
    def __str__(self):
        return self.Tourist_Guide_Name