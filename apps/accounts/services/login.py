from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from rest_framework.response import Response

def login_user(serializers):
    e_mail = serializers.validated_data['Email']
    password = serializers.validated_data['Password']
        
    try:
        user = User.objects.get(email = e_mail)
    except User.DoesNotExist:
        raise ValidationError({'Message':'Signup an account first!'})
        
    if check_password(password, user.password):
        return user
    
    raise ValidationError({'Message':'Invalid Credentials!'})