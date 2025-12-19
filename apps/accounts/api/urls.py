from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('signup/', views.UserModelSerializersView.as_view(), name='UserModelSerializersView'),
    path('login/', views.LoginSerializersView.as_view(), name='LoginSerializersView'),
]
