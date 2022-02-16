from django.core.exceptions import PermissionDenied
from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and obj.author == request.user:
            return True
        else:
            raise PermissionDenied('Изменение чужого контента запрещено!')
