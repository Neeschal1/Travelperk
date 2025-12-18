from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='TokenRefreshView'),
    path('accounts/', include('apps.accounts.api.urls'))
]