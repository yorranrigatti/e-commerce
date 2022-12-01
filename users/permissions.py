from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class isSuperuser(permissions.IsAdminUser):
    def has_permission(self, request, _):
        return bool(request.user and request.user.is_superuser)


class isSuperuserOrOwner(BasePermission):
    def has_object_permission(self, request, _, obj):
        if bool(request.user and request.user.is_superuser):
            return True
        return request.user == obj


class isSuperUserOrSafeMethod(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_superuser)
