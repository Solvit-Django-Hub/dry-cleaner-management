from rest_framework.permissions import BasePermission


class IsAdminOrStaff(BasePermission):
    """
    Allow access only to admin and staff users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in ["ADMIN", "STAFF"]
        )


class IsCustomer(BasePermission):
    """
    Allow access only to customer users.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "CUSTOMER"
        )


class IsOwnerOrAdminStaff(BasePermission):
    """
    Allow users to access their own object.
    Admins and staff can access any object.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.user == request.user

class IsOrderOwnerOrAdminStaff(BasePermission):
    """
    Allow customers to access their own orders.
    Admins and staff can access any order.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        if request.user.role in ["ADMIN", "STAFF"]:
            return True

        return obj.customer.user == request.user


class IsOrderItemOwnerOrAdminStaff(BasePermission):
    """
    Allow customers to access order items belonging to their own orders.
    Admins and staff can access any order item.
    """

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