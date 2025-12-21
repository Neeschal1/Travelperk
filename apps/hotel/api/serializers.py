from rest_framework import serializers
from apps.hotel.models.entities import Hotel
from apps.hotel.services.create import create_new_hotel_data_record
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class HotelSerializer(serializers.ModelSerializer):
    Hotel_Owner_Username = serializers.CharField()
    class Meta:
        model = Hotel
        fields = '__all__'
        extra_kwargs = {
            'Hotel_Name' : {'required' : True},
            'Hotel_Category_In_Stars' : {'required' : True},
            'Hotel_Location' : {'required' : True},
            'Total_Rooms_Available' : {'required' : True},
            'Room_Description' : {'required' : True},
            'Room_Rent_Per_Day_In_Nepali_Rupees' : {'required' : True},
        }
        
    def create(self, validated_data):
        owner_username = validated_data.pop('Hotel_Owner_Username')
        try:
            user = User.objects.get(username = owner_username)
        except User.DoesNotExist:
            raise ValidationError('User not found. Try again!')
        
        if user.is_active != True:
            raise ValidationError({'Message':'You are not verified yet. Contact with Traveperk admin and tell him/her to verify your account and then try again! Thank you :)'})
        
        result = create_new_hotel_data_record(validated_data, user)
        return result
        
