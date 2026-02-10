from django.urls import path
from . import views

urlpatterns = [
    path('', views.tourist_guides_home, name='tourist_guides_home')
]
