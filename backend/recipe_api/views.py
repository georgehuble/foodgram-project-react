from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

from .models import Ingredient, Recipe, Tag
from .serializers import IngredientSerializer, RecipeSerializer, TagSerializer


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
