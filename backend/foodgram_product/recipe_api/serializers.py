from rest_framework import serializers
from .models import Tag, Ingredient, Recipe
from user_api.serializers import UserDetailSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'color', 'slug')
        model = Tag


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'amount', 'measurement_unit')
        model = Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    tag = TagSerializer(read_only=True, many=True)
    ingredients = IngredientSerializer(read_only=True, many=True)
    author = UserDetailSerializer(read_only=True)

    class Meta:
        fields = ('author', 'name', 'image',
                  'text', 'ingredients', 'tag', 'cooking_time')
        model = Recipe


# class FavoriteSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'name', 'image', 'cooking_time')
#         model = Recipe
