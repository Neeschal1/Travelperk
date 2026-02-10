from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserModelSerializers, LoginSerializers
from .initial_ui import initial_ui_page
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from apps.accounts.services.login import login_user
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

def accounts_home(request):
    return HttpResponse(initial_ui_page)
    
class UserModelSerializersView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserModelSerializers
    
class LoginSerializersView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializers = LoginSerializers(data = request.data)
        serializers.is_valid(raise_exception=True)
        
        user = login_user(serializers) 
        refresh = RefreshToken.for_user(user)
        
        if user:
            return Response({
                'Access Token':str(refresh.access_token),
                'Refresh Token' : str(refresh),
                'User' : {
                'Message':f'Hi, {user.first_name}! You logged in successfully!'}})
            