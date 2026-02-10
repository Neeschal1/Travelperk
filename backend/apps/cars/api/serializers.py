from rest_framework import serializers
from apps.cars.models.entities import Car
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from apps.cars.services.create import create_new_car_data

class CarSerializers(serializers.ModelSerializer):
    Car_Owner_Username = serializers.CharField()
    class Meta:
        model = Car
        fields = '__all__'
        extra_kwargs = {
            'Car_Name' : {'required' : True},
            'Car_Owner' : {'required' : True},
            'Car_Model' : {'required' : True},
            'Car_Seats' : {'required' : True},
            'Car_Color' : {'required' : True},
        }
    
    def create(self, validated_data):
        carowner = validated_data.pop('Car_Owner_Username')
        try:
            owner = User.objects.get(username = carowner)
        except Car.DoesNotExist:
            raise ValidationError({'Message':'User does not exist. Sorry!'})
        
        if owner.is_active != True:
            raise ValidationError({'Message':'You are not verified yet. Contact with Traveperk admin and tell him/her to verify your account and then try again! Thank you :)'})
            
        car_detail = create_new_car_data(validated_data, owner)
        
        return car_detail
        