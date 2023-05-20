from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, obj):
        print(obj)
        print(request)
        return bool(obj.pk == request.user.pk)