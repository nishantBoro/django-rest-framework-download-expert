from django.utils.encoding import smart_str
from rest_framework import permissions


class IsGroupUser(permissions.BasePermission):

    def has_permission(self, request, view):
        group_name = getattr(view, 'group_name')
        return request.user.groups.filter(name=smart_str(group_name)).exists()
