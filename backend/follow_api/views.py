from django.db.utils import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from recipe_api.models import Recipe
from rest_framework import mixins, permissions, status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from user_api.models import CustomUser

from . import serializers
from .models import Favourite, Shopping, Subscribe
from .serializers import FavouriteSerializer, SubscribeSerializer


class FavouriteView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavouriteSerializer
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        name = get_object_or_404(Recipe, id=self.kwargs.get('id'))
        try:
            Favourite.objects.create(user=request.user, name=name)
            serializer = serializers.FavouriteSerializer(
                name, context={'request': request})
        except IntegrityError:
            return Response('Этот рецепт уже добавлен в избранное.'
                            ' Неправильный запрос.',
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        Favourite.objects.filter(user=request.user.pk,
                                 name=self.kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscribeView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubscribeSerializer
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        author = get_object_or_404(CustomUser, id=self.kwargs.get('id'))
        serializer_user = SubscribeSerializer
        try:
            if author == request.user:
                return Response('Нельзя подписаться на себя самого.'
                                ' Неверный запрос.',
                                status=status.HTTP_400_BAD_REQUEST)
            Subscribe.objects.create(user=request.user, author=author)
            serializer = serializer_user(
                author, context={'request': request})
        except IntegrityError:
            return Response('Вы уже подписаны на данного пользователя.'
                            ' Неверный запрос.',
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        Subscribe.objects.filter(user=request.user.pk,
                                 author=self.kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SubscribeListView(mixins.ListModelMixin,
                        GenericViewSet):
    serializer_class = SubscribeSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(following__user=self.request.user)


class ShoppingView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavouriteSerializer
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        name = get_object_or_404(Recipe, id=self.kwargs.get('id'))
        try:
            Shopping.objects.create(user=request.user, name=name)
            serializer = serializers.FavouriteSerializer(
                name, context={'request': request})
        except IntegrityError:
            return Response('Этот рецепт уже есть в списке покупок.'
                            ' Неправильный запрос.',
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        Shopping.objects.filter(user=request.user.pk,
                                name=self.kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
