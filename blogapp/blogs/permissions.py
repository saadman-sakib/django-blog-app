from rest_framework.permissions import BasePermission, SAFE_METHODS

#custom permission
class IsAuthorOrAnonReadOnly(BasePermission):
    message = 'editing and deleting is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user
