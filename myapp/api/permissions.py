from rest_framework.permissions import BasePermission

class isClientUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)

class isCustomerUser(BasePermission):
    def has_permission(self, request, view):

        return bool(request.user and request.user.is_client)        