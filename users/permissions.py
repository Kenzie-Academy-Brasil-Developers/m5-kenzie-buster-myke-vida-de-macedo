from rest_framework import permissions
from rest_framework.views import Request

class UserPermission(permissions.BasePermission):
    def has_object_permission(self, req, view, obj):

        if req._user.is_employee:
            return True

        return obj == req._user