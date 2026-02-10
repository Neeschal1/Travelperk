from django.urls import path
from . import views

urlpatterns = [
    path('', views.verifications_home, name='verifications_home')
]
