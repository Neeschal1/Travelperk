from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

schema_view = get_schema_view(
    openapi.Info(
        title="TravelPerk API",
        default_version='v1',
        description="API documentation for TravelPerk backend",
    ),
    public=True,
    permission_classes=(permissions.IsAdminUser, ),
    authentication_classes=(SessionAuthentication, BasicAuthentication),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='TokenObtainPairView'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='TokenRefreshView'),
    path('accounts/', include('apps.accounts.api.urls')),
    path('ai_assistant/', include('apps.ai_assistant.api.urls')),
    path('bookings/', include('apps.bookings.api.urls')),
    path('cars/', include('apps.cars.api.urls')),
    path('cuisines/', include('apps.cuisines.api.urls')),
    path('flights/', include('apps.flights.api.urls')),
    path('hotels/', include('apps.hotel.api.urls')),
    path('payments/', include('apps.payments.api.urls')),
    path('guides/', include('apps.touristguide.api.urls')),
    path('destination/', include('apps.travel_destinations.api.urls')),
    path('verification/', include('apps.verifications.api.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]