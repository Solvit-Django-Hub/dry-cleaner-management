from rest_framework import generics

from accounts.permissions import (
    IsAdminStaffOrReadOnlyCustomer,
    IsNotificationOwnerOrAdminStaff,
)

from .models import Notification
from .serializers import NotificationSerializer


class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminStaffOrReadOnlyCustomer]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Notification.objects.all()

        return Notification.objects.filter(
            customer__user=user
        )


class NotificationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [
        IsAdminStaffOrReadOnlyCustomer,
        IsNotificationOwnerOrAdminStaff,
    ]