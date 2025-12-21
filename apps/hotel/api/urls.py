from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotel_home, name='hotel_home'),
    path('hotel/', views.HotelSerializerView.as_view(), name='HotelSerializerView')
]
