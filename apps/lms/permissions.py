from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        print(f'user - {request.user}, obj - {obj}, owner - {obj.user}')
        return request.user == obj.user
