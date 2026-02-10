from django.urls import path
from . import views

urlpatterns = [
    path('', views.packages_home, name='packages_home')
]
