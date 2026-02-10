from django.http import HttpResponse
from .initial_ui import initial_ui_page
from rest_framework import generics
from apps.hotel.models.entities import Hotel
from .serializers import HotelSerializer

def hotel_home(request):
    return HttpResponse(initial_ui_page)
    
class HotelSerializerView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer