from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from backend_app.api.serializers import TaskSerializer
from backend_app.models import Tasks

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class=TaskSerializer