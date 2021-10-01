from recipe_api.views import StandardResultsSetPagination
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from .models import CustomUser
from .serializers import UserSerializer


class MixinsViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    pass


class UserViewSet(MixinsViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'
    pagination_class = StandardResultsSetPagination
