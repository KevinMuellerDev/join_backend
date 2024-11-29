from rest_framework import serializers
from django.contrib.auth.models import User
import re


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    username = serializers.CharField(max_length=150, validators=[])

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'repeated_password']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_username(self, value):
        if not re.match(r'^[\w\s]+$', value):
            raise serializers.ValidationError(
                {"error": "username isn't allowed to contain other than Characters, numbers and whitespaces"}
            )
        return value

    def save(self):
        pw = self.validated_data['password']
        repeated_pw = self.validated_data['repeated_password']
        if pw != repeated_pw:
            raise serializers.ValidationError(
                {'error': 'Passwords dont match'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'email already exists'})

        account = User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],)
        
        account.set_password(pw)
        account.save()
        return account
