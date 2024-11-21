from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from backend_app.api.serializers import TaskSerializer, ContactsSerializer
from backend_app.models import Tasks, Contacts
from .permissions import IsStaffOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskSummaryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tasks.objects.all()
    permission_classes=[IsStaffOrReadOnly]

    def list(self, request):
        data = {
            "total_tasks": self.queryset.count(),
            "todo": self.queryset.filter(await_feedback=False, in_progress=False, done=False).count(),
            "in_progress": self.queryset.filter(in_progress=True).count(),
            "await_feedback": self.queryset.filter(await_feedback=True).count(),
            "done": self.queryset.filter(done=True).count(),
        }

        return Response(data)


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
