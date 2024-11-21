from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS
