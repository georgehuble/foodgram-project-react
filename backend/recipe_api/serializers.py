from follow_api.models import Favourite, Shopping
from rest_framework import serializers
from user_api.serializers import UserDetailSerializer

from .models import Ingredient, Recipe, Tag, IngredientInRecipe


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'color', 'slug')
        model = Tag


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'measurement_unit')
        model = Ingredient

#
# class RecipeSerializer(serializers.ModelSerializer):
#     tag = TagSerializer(read_only=True, many=True)
#     ingredients = IngredientSerializer(read_only=True, many=True)
#     author = UserDetailSerializer(read_only=True)
#     is_favorited = serializers.SerializerMethodField('check_if_is_favorited')
#     is_in_shopping_cart = serializers.SerializerMethodField('check_if_is_in_shopping_cart')
#
#     def check_if_is_favorited(self, obj):
#         user = self.context.get('request').user
#         return Favourite.objects.filter(user=user, name=obj).exists()
#
#     def check_if_is_in_shopping_cart(self, obj):
#         user = self.context.get('request').user
#         return Shopping.objects.filter(user=user, name=obj).exists()
#
#     class Meta:
#         model = Recipe
#         fields = ('author', 'name', 'image',
#                   'text', 'ingredients', 'tag',
#                   'cooking_time', 'is_favorited',
#                   'is_in_shopping_cart')


class AddIngredientToRecipeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='ingredient.id')

    class Meta:
        model = IngredientInRecipe
        fields = ('id', 'amount')


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = AddIngredientToRecipeSerializer(many=True)
    tags = serializers.SlugRelatedField(
        many=True,
        queryset=Tag.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Recipe
        fields = '__all__'
