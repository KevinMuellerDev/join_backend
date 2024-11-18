from rest_framework import serializers, status
from backend_app.models import Tasks, Contacts, Summary, Subtask


class ContactsSerializer(serializers.ModelSerializer):
    assigned = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Contacts
        fields = ['id', 'name', 'lastname', 'initials',
                  'email', 'phone', 'circle_color', 'assigned']


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

        if subtasks_data:
            instance.subtasks.all().delete()
            for subtask_data in subtasks_data:
                subtask_data['task'] = instance
                Subtask.objects.create(task=instance, **subtask_data)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Ersetze die 'assigned'-Felder mit den Namen der Kontakte
        representation['assigned'] = [
            contact.name for contact in instance.assigned.all()
        ]

        representation['subtasks'] = [
            {'task_description': subtask.task_description, 'task_state': subtask.task_state}
            for subtask in instance.subtasks.all()
        ]

        return representation
