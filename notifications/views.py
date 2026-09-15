from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsNotificationOwnerOrAdminStaff
from .models import Notification
from .serializers import NotificationSerializer


class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Notification.objects.all()

        return Notification.objects.filter(customer__user=user)


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [
        IsAuthenticated,
        IsNotificationOwnerOrAdminStaff,
    ]