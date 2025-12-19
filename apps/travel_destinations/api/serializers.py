from rest_framework import serializers
from apps.travel_destinations.models.entities import Desired_Travel_Destination
from apps.travel_destinations.services.create import create_new_travel_destiny
from django.contrib.auth.models import User

class DesiredTravelDestinationSerializers(serializers.ModelSerializer):
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
        # user = self.context['request'].user
        
        desire = create_new_travel_destiny(validated_data)
        return {
            'Message' : f'{desire}'
        }