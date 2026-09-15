from rest_framework import serializers

from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "amount",
            "method",
            "status",
            "paid_at",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]