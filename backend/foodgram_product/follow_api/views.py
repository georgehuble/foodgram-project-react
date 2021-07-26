from django.db.utils import IntegrityError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, \
    status, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import serializers
from .models import Favourite, Subscribe
from .serializers import FavouriteSerializer, \
    SubscribeSerializer
from recipe_api.models import Recipe
from user_api.models import CustomUser


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
            return Response('Этот рецепт уже есть в избранном.'
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
            Subscribe.objects.create(user=request.user, author=author)
            serializer = serializer_user(
                author, context={'request': request})
        except IntegrityError:
            return Response('Вы уже подписаны на данного пользователя.'
                            ' Неправильный запрос.',
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(data=serializer.data,
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        Subscribe.objects.filter(user=request.user.pk,
                                 author=self.kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
