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