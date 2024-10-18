from rest_framework import permissions
from rest_framework.decorators import permission_classes


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    message = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsSubscriber(permissions.BasePermission):
    """Проверяет, является ли пользователь подписчиком."""

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False
