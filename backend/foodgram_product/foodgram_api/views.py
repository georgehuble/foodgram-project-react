from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_simplejwt.views import TokenViewBase
from django.db import models

from .models import Recipe, CustomUser
from .serializers import (TegSerializer,
                          IngredientSerializer,
                          RecipeSerializer,
                          TokenObtainPairNoPasswordSerializer,
                          TokenRefreshNoPassworSerializer,
                          UsersSerializer)

User = get_user_model()


class MixinsViewSet(mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    GenericViewSet):
    pass


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'username'

    @action(detail=False, methods=['GET', 'PATCH'],
            permission_classes=[IsAuthenticated])
    def me(self, request):
        instance = request.user
        serializer = self.get_serializer(instance)
        if request.method == 'PATCH':
            serializer = self.get_serializer(instance,
                                             data=request.data,
                                             partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        return Response(serializer.data)


class TokenObtainPairNoPasswordView(TokenViewBase):
    serializer_class = TokenObtainPairNoPasswordSerializer


class TokenRefreshNoPasswordView(TokenViewBase):
    serializer_class = TokenRefreshNoPassworSerializer


class RecipeListView(MixinsViewSet):
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend, )
    permission_classes = [permissions.IsAuthenticated]
    paginate_by = 6
