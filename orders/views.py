from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import (
    IsAdminOrStaff,
    IsOrderItemOwnerOrAdminStaff,
    IsOrderOwnerOrAdminStaff,
)
from .models import ClothingItem, Order, OrderItem
from .serializers import (
    ClothingItemSerializer,
    OrderItemSerializer,
    OrderSerializer,
)


class ClothingItemListCreateView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
    permission_classes = [IsAdminOrStaff]


class ClothingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer
    permission_classes = [IsAdminOrStaff]


class OrderListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Order.objects.all()

        return Order.objects.filter(customer__user=user)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        IsAuthenticated,
        IsOrderOwnerOrAdminStaff,
    ]


class OrderItemListCreateView(generics.ListCreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return OrderItem.objects.all()

        return OrderItem.objects.filter(order__customer__user=user)


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [
        IsAuthenticated,
        IsOrderItemOwnerOrAdminStaff,
    ]