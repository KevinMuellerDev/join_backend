from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend_app.api.views import TaskViewSet,TaskSummaryViewSet,ContactsViewSet


router=routers.SimpleRouter()
router.register(r'tasks',TaskViewSet)
router.register(r'contacts',ContactsViewSet)
router.register(r'summary',TaskSummaryViewSet, basename='summary')

urlpatterns = [
    path('',include(router.urls)),
]
