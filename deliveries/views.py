from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsDeliveryOwnerOrAdminStaff
from .models import Delivery
from .serializers import DeliverySerializer


class DeliveryListCreateView(generics.ListCreateAPIView):
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Delivery.objects.all()

        return Delivery.objects.filter(order__customer__user=user)


class DeliveryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [
        IsAuthenticated,
        IsDeliveryOwnerOrAdminStaff,
    ]