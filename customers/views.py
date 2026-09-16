from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsOwnerOrAdminStaff
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListCreateView(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Customer.objects.all()

        return Customer.objects.filter(user=user)


class CustomerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminStaff]