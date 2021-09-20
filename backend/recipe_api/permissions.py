from rest_framework.permissions import AllowAny


class MyCustomPermission(AllowAny):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return bool(request.user and request.user.is_authenticated)
