import datetime
from wsgiref.util import FileWrapper
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions
from rest_framework.viewsets import GenericViewSet
from rest_framework.pagination import PageNumberPagination

from .models import Tag, Recipe, Ingredient
from .serializers import (TagSerializer,
                          IngredientSerializer,
                          RecipeSerializer)
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from rest_framework.response import Response


class TalentSearchpagination(PageNumberPagination):
    page_size = 6


class MixinsViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    pass


class RecipeListView(MixinsViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('author', 'name')
    permission_classes = [permissions.AllowAny]
    pagination_class = TalentSearchpagination


class IngredientListView(MixinsViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [permissions.AllowAny]
    pagination_class = TalentSearchpagination


class TagsView(MixinsViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [permissions.AllowAny]


class IngredientDownloadView(MixinsViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (DjangoFilterBackend,)
    permission_classes = [permissions.IsAuthenticated]

    def create_file(self):
        shop_list = open('../media/file/shop_list.txt', 'w+')
        shop_list.write('Привет, список покупок!')
        shop_list.close()
