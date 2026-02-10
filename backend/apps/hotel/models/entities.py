from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    Hotel_Name = models.CharField(max_length=100)
    Hotel_Owner_Username = models.ForeignKey(User, on_delete=models.CASCADE)
    Hotel_Category_In_Stars = models.IntegerField(default=2, blank=True)
    Hotel_Location = models.CharField(max_length=100)
    Total_Rooms_Available = models.IntegerField(default=10, blank=True)
    Room_Description = models.TextField()
    Room_Rent_Per_Day_In_Nepali_Rupees = models.IntegerField(default=2000, blank=True)
    
    def __str__(self):
        return self.Hotel_Name