from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from backend_app.api.views import TaskViewSet,ContactsViewSet


router=routers.SimpleRouter()
router.register(r'tasks',TaskViewSet)
router.register(r'contacts',ContactsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]
