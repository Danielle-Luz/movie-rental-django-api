from rest_framework import permissions
from .models import User


class UserInfoPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: User):
        return request.user.is_authenticated and (
            request.user.is_employee or request.user.email == obj.email
        )
