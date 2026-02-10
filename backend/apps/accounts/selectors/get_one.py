from rest_framework.views import APIView
from django.contrib.auth.models import User
from apps.accounts.selectors.singleuserserializers import SingleUserSerializers
from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

class GetOneUserDetails(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializers = SingleUserSerializers(data = request.data)
        serializers.is_valid(raise_exception=True)
        
        user_name = serializers.validated_data['Username']
        
        try:
            user = User.objects.get(username = user_name)
        except User.DoesNotExist:
            raise ValidationError({'Message':'Username does not exists!'})
        
        return Response({
            'User' : {
                'First Name' : user.first_name,
                'Last Name' : user.last_name,
                'Username' : user.username,
                'Email' : user.email,
                'Password' : user.password,
            }
        })