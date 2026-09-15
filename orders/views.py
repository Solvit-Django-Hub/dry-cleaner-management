from rest_framework import generics

from .models import ClothingItem, Order, OrderItem
from .serializers import (
    ClothingItemSerializer,
    OrderItemSerializer,
    OrderSerializer,
)


class ClothingItemListCreateView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemListCreateView(generics.ListCreateAPIView):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer 
