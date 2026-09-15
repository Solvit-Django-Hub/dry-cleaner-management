from rest_framework import generics

from .models import ClothingItem, Order
from .serializers import ClothingItemSerializer, OrderSerializer


class ClothingItemListCreateView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class ClothingItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer