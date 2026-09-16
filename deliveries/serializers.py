from rest_framework import serializers

from .models import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = [
            "id",
            "order",
            "delivery_address",
            "status",
            "delivery_date",
            "delivered_at",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
        ]