from django.http import HttpResponse
from .initial_ui import initial_ui_page
from .serializers import DesiredTravelDestinationSerializers
from apps.travel_destinations.models.entities import Desired_Travel_Destination
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

def travel_destinations_home(request):
    return HttpResponse(initial_ui_page)

class DesiredTravelDestinationSerializersListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Desired_Travel_Destination.objects.all()
    serializer_class = DesiredTravelDestinationSerializers