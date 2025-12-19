from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ValidationError

def signup_user(validated_data):
    First_Name = validated_data['first_name']
    Last_Name = validated_data['last_name']
    Username = validated_data['username']
    Email = validated_data['email']
    Password = validated_data['password']
    
    # Hashing the password for security purpose
    hashed_password = make_password(Password)
    
    if User.objects.filter(email = Email).exists():
        raise ValidationError({'Message':f'Your email: {Email} is already registered with another account. Try another email. Thank you!'})
    
    user = User.objects.create(
        first_name = First_Name,
        last_name = Last_Name,
        username = Username,
        email = Email,
        password = hashed_password,
        is_active = False
    )
    
    return user