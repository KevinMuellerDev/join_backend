from .serializers import RegistrationSerializer
from backend_app.models import Contacts
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
import random

class RegistrationView(APIView):
    permission_classes=[AllowAny]

    def post(self,request):
        serializer = RegistrationSerializer(data=request.data)
        statusCode=None
        data={}

        if serializer.is_valid():
            saved_account = serializer.save()
            token,created = Token.objects.get_or_create(user=saved_account)
            data={
                'token':token.key,
                'username':saved_account.username,
                'email':saved_account.email
            }
            r = lambda: random.randint(0,255)
            color = '#%02X%02X%02X' % (r(),r(),r())
            Contacts.objects.create(name=saved_account.username, email=saved_account.email, initials=saved_account.username[0][0].upper(),circle_color=color)
            statusCode = status.HTTP_201_CREATED
        else:
            data=serializer.errors
            statusCode = status.HTTP_409_CONFLICT

        return Response(data,status=statusCode)

class CustomLoginView(ObtainAuthToken):
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        statusCode= None
        data = {}
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
            statusCode=status.HTTP_202_ACCEPTED
        else:
            data = serializer.errors
            statusCode=status.HTTP_400_BAD_REQUEST
        return Response(data,status=statusCode)    
