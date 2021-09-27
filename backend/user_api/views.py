from rest_framework import mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import CustomUser
from .serializers import UserDetailSerializer, UsersSerializer


class MixinsViewSet(mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    pass


class UsersViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]
    lookup_field = 'username'


class UserDetailViewSet(ModelViewSet):
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.kwargs.get('id'))
