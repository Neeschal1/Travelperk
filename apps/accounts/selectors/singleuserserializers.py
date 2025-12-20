from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SingleUserSerializers(serializers.Serializer):
    Username = serializers.CharField()