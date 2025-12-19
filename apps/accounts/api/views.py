from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserModelSerializers
from .initial_ui import initial_ui_page

def accounts_home(request):
    return HttpResponse(initial_ui_page)
    
class UserModelSerializersView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializers