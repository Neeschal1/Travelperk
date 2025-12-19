from django.urls import path
from . import views

urlpatterns = [
    path('', views.ai_assistant_home, name='ai_assistant_home')
]
