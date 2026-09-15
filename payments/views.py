from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsPaymentOwnerOrAdminStaff
from .models import Payment
from .serializers import PaymentSerializer


class PaymentListCreateView(generics.ListCreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role in ["ADMIN", "STAFF"]:
            return Payment.objects.all()

        return Payment.objects.filter(order__customer__user=user)


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [
        IsAuthenticated,
        IsPaymentOwnerOrAdminStaff,
    ]