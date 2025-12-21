from rest_framework import serializers
from apps.travel_destinations.models.entities import Desired_Travel_Destination
from apps.travel_destinations.services.create import create_new_travel_destiny
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class DesiredTravelDestinationSerializers(serializers.ModelSerializer):
    username = serializers.CharField(write_only = True)
    class Meta:
        model = Desired_Travel_Destination
        fields = '__all__'
        extra_kwargs = {
            'user' : {'read_only' : True},
            'Dream_Continent' : {'required' : True},
            'Trip_Difficulty' : {'required' : True},
            'Interest' : {'required' : True},
            'Trip_Category' : {'required' : True},
            'Accomodation' : {'required' : True},
        }
        
    def create(self, validated_data):
        username = validated_data.pop('username')
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            raise ValidationError({'Message':'User not found!'})

        desire = create_new_travel_destiny(validated_data, user)
        return desire