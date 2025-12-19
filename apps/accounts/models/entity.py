from django.db import models

class OTPVerification(models.Model):
    OTP = models.IntegerField()
    User_Email = models.EmailField()
    
    def __str__(self):
        return self.User_Email