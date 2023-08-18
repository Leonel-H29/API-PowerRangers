from rest_framework import permissions


class SuperuserPermission(permissions.BasePermission):
    """
    Clase para determinar los permisos del superusuario de la aplicación
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser and permissions.IsAuthenticated


class ReadOnlyPermission(permissions.BasePermission):
    """
    Clase para determinar los permisos del usuario comun dentro de la aplicación
    """

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
