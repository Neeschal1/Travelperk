from django.urls import path
from . import views
from apps.accounts.selectors import list, get_one

urlpatterns = [
    path('', views.accounts_home, name='accounts_home'),
    path('signup/', views.UserModelSerializersView.as_view(), name='UserModelSerializersView'),
    path('login/', views.LoginSerializersView.as_view(), name='LoginSerializersView'),
    path('listusers/', list.ListAllUsersAPIView.as_view(), name='ListAllUsersAPIView'),
    path('singleuser/', get_one.GetOneUserDetails.as_view(), name='GetOneUserDetails')
]