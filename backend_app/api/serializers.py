from rest_framework import serializers, status
from backend_app.models import Tasks, Contacts, Summary, Subtask
from django.contrib.auth.models import User
import random


class ContactsSerializer(serializers.ModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Contacts
        fields = ['id', 'name', 'initials',
                  'email', 'phone', 'circle_color', 'assigned', 'user']

    def create(self, validated_data):

        def r(): return random.randint(0, 255)
        color = '#%02X%02X%02X' % (r(), r(), r())
        validated_data['circle_color'] = color
        contact = Contacts.objects.create(**validated_data)
        return contact


class SubtaskSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Subtask
        fields = ('id', 'task_description', 'task_state', 'task')


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = Tasks
        fields = ['id', 'category', 'title', 'description',
                  'duedate', 'created', 'priority', 'in_progress',
                  'await_feedback', 'done', 'assigned', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_data = validated_data.pop('assigned', [])

        task = Tasks.objects.create(**validated_data)

        task.assigned.set(assigned_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_data = validated_data.pop('assigned', None)

        instance.category = validated_data.get('category', instance.category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.duedate = validated_data.get('duedate', instance.duedate)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.await_feedback = validated_data.get(
            'await_feedback', instance.await_feedback)
        instance.in_progress = validated_data.get(
            'in_progress', instance.in_progress)
        instance.done = validated_data.get('done', instance.done)

        instance.save()

        if assigned_data is not None:
            instance.assigned.set(assigned_data)

        existing_subtasks = {subtask.id: subtask for subtask in instance.subtasks.all()}
        updated_subtasks_ids = []  

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')

            if subtask_id and subtask_id in existing_subtasks:
                subtask_instance = existing_subtasks[subtask_id]
                subtask_instance.task_description = subtask_data.get(
                    'task_description', subtask_instance.task_description)
                subtask_instance.task_state = subtask_data.get(
                    'task_state', subtask_instance.task_state)
                subtask_instance.save()
                updated_subtasks_ids.append(subtask_id)
            else:
                Subtask.objects.create(task=instance, **subtask_data)

        for subtask_id, subtask_instance in existing_subtasks.items():
            if subtask_id not in updated_subtasks_ids:
                subtask_instance.delete()

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['assigned'] = [
            {'id': contact.id, 'name': contact.name, 'initials': contact.initials, 'circle_color': contact.circle_color} for contact in instance.assigned.all()
        ]

        representation['subtasks'] = [
            {'id': subtask.id, 'task_description': subtask.task_description,
                'task_state': subtask.task_state}
            for subtask in instance.subtasks.all()
        ]

        return representation
