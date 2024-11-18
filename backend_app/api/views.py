from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from backend_app.api.serializers import TaskSerializer,ContactsSerializer
from backend_app.models import Tasks, Contacts

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class=TaskSerializer
    
class ContactsViewSet(viewsets.ModelViewSet):
    queryset= Contacts.objects.all()
    serializer_class=ContactsSerializer