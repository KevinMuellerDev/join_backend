from rest_framework import serializers, status
from backend_app.models import Tasks,Contacts,Summary


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        exclude=[]