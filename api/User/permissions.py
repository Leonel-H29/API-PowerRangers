from rest_framework import permissions

class SuperuserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

class ReadOnlyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
