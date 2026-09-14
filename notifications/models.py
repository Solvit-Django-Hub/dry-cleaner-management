from django.db import models
from customers.models import Customer


class Notification(models.Model):

    class Type(models.TextChoices):
        ORDER_RECEIVED = "ORDER_RECEIVED", "Order Received"
        ORDER_READY = "ORDER_READY", "Order Ready"
        ORDER_COLLECTED = "ORDER_COLLECTED", "Order Collected"
        DELIVERY_UPDATE = "DELIVERY_UPDATE", "Delivery Update"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=Type.choices,
    )

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message