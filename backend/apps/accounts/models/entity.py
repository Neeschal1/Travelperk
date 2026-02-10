from django.db import models

class ForgotPassword(models.Model):
    User_Email = models.EmailField()
    Password = models.CharField(max_length=180)
    
    def __str__(self):
        return self.User_Email