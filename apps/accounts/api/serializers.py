from django.contrib.auth.models import User
from ..models import OTPVerification
from rest_framework import serializers
from rest_framework.response import Response
from apps.accounts.services.create import create_user

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'date_joined']
        extra_kwargs = {
            'first_name' : {'required' : True,},
            'last_name' : {'required' : True,},
            'username' : {'required' : True  },
            'email' : {'required' : True,}, 
            'password' : {'required' : True,'write_only' : True},
            'is_active' : {'read_only' : True},
            'date_joined' : {'read_only' : True}
        }
    
    def create(self, validated_data):
        user = create_user(validated_data)
        return user
        # return Response{
        # 'Data' : user,
        # 'Message' : 'Your request of verifying your account has been sent to the database admin. We will let you know when your account will be verified. Stay patient!'
    # }