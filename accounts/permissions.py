from rest_framework.permissions import BasePermission


class IsAdminOrStaff(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["ADMIN", "STAFF"]
        )


class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "CUSTOMER"
        )


class IsOwnerOrAdminStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.user == request.user


class IsOrderOwnerOrAdminStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.customer.user == request.user


class IsOrderItemOwnerOrAdminStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.order.customer.user == request.user


class IsPaymentOwnerOrAdminStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.order.customer.user == request.user


class IsDeliveryOwnerOrAdminStaff(BasePermission):
    """
    Allow customers to access deliveries for their own orders.
    Admins and staff can access any delivery.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.order.customer.user == request.user


class IsNotificationOwnerOrAdminStaff(BasePermission):
    """
    Allow customers to access their own notifications.
    Admins and staff can access any notification.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.customer.user == request.user