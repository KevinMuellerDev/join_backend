from rest_framework import serializers, status
from backend_app.models import Tasks, Contacts, Summary


class TaskSerializer(serializers.ModelSerializer):
    assigned = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Tasks
        fields = ['id', 'category', 'title', 'description',
                  'duedate', 'created', 'priority', 'in_progress',
                  'await_feedback', 'done', 'assigned', 'subtasks']


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        exclude = []
