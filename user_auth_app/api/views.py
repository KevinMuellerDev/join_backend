from .serializers import RegistrationSerializer,LoginSerializer
from backend_app.models import Contacts
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
        else:
            data=serializer.errors

        return Response(data)

class CustomLoginView(ObtainAuthToken):
    permission_classes=[AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        statusCode=0
        data = {}
        print('sieht man mich?')
        if serializer.is_valid():
            print('bin trotzdem da')
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            data = {
                'token': token.key,
                'username': user.username,
                'email': user.email
            }
            statusCode=200
        else:
            data = serializer.errors
            statusCode=400
        return Response(data,status=statusCode)    
