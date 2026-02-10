from django.contrib.auth.models import User
from rest_framework import generics
from apps.accounts.api.serializers import UserModelSerializers
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ListAllUsersAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserModelSerializers