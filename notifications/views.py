from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListCreateView(generics.ListCreateAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
