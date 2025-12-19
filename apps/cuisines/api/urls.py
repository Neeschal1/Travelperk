from django.urls import path
from . import views

urlpatterns = [
    path('', views.cuisines_home, name='cuisines_home')
]
