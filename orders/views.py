from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import ClothingItem
from .serializers import ClothingItemSerializer


class ClothingItemListCreateView(generics.ListCreateAPIView):
    queryset = ClothingItem.objects.all()
    serializer_class = ClothingItemSerializer