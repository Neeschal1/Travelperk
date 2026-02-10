from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response
from apps.accounts.services.signup import signup_user
from django.contrib.auth.hashers import check_password

class UserModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'password', 'is_active', 'date_joined']
        extra_kwargs = {
            'id' : {'read_only' : True},
            'first_name' : {'required' : True,},
            'last_name' : {'required' : True,},
            'username' : {'required' : True  },
            'email' : {'required' : True,}, 
            'password' : {'required' : True,'write_only' : True},
            'is_active' : {'read_only' : True},
            'date_joined' : {'read_only' : True}
        }
    def create(self, validated_data):
        user = signup_user(validated_data)
        return user
    
class LoginSerializers(serializers.Serializer):
    Email = serializers.EmailField()
    Password = serializers.CharField()
    
