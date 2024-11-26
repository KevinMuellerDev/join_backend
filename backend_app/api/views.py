from datetime import datetime
from django.shortcuts import get_object_or_404
import locale
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from backend_app.api.serializers import TaskSerializer, ContactsSerializer
from backend_app.models import Tasks, Contacts
from .permissions import ReadOnly,IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskSummaryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Tasks.objects.all()
    permission_classes=[IsAuthenticated]

    def list(self, request):
        urgent_tasks = self.queryset.filter(priority="urgent")
        urgent_tasks_upcoming = urgent_tasks.filter(duedate__gte=datetime.now().date()).order_by('duedate')
        next_task = urgent_tasks_upcoming.first()
        date_obj = next_task.duedate
        locale.setlocale(locale.LC_TIME, "de_DE.UTF-8")
        formatted_date_de = date_obj.strftime("%B %d, %Y")

        data = {
            "total_tasks": self.queryset.count(),
            "todo": self.queryset.filter(await_feedback=False, in_progress=False, done=False).count(),
            "in_progress": self.queryset.filter(in_progress=True).count(),
            "await_feedback": self.queryset.filter(await_feedback=True).count(),
            "done": self.queryset.filter(done=True).count(),
            "urgent":self.queryset.filter(priority="high").count(),
            "urgent_date":formatted_date_de
        }

        return Response(data)


class ContactsViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
