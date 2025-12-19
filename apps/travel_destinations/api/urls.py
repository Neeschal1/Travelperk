from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_destinations_home, name='travel_destinations_home')
]
