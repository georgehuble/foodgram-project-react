from follow_api.models import Favourite, Shopping
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from user_api.serializers import UserDetailSerializer

from .models import Ingredient, IngredientInRecipe, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name', 'color', 'slug')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'measurement_unit')

    def to_internal_value(self, data):
        return Ingredient.objects.get(id=data)


class AddIngredientToRecipeSerializer(serializers.ModelSerializer):
    id = ReadOnlyField(source='ingredient.id')
    ingredient = ReadOnlyField(source='ingredient.name')
    measurement_unit = ReadOnlyField(source='ingredient.measurement_unit')

    class Meta:
        model = IngredientInRecipe
        fields = ['id', 'ingredient', 'measurement_unit', 'amount']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = AddIngredientToRecipeSerializer(source='ingredientinrecipe_set',
                                                  many=True,
                                                  required=True)
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
    author = UserDetailSerializer(read_only=True)
    is_favorited = serializers.SerializerMethodField('check_if_is_favorited')
    is_in_shopping_cart = serializers.SerializerMethodField('check_if_is_in_shopping_cart')

    def check_if_is_favorited(self, obj):
        user = self.context.get('request').user
        return Favourite.objects.filter(user=user, name=obj).exists()

    def check_if_is_in_shopping_cart(self, obj):
        user = self.context.get('request').user
        return Shopping.objects.filter(user=user, name=obj).exists()

    def create(self, validated_data):
        ingredients = self.context['request'].data['ingredients']
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        for ingredient in ingredients:
            IngredientInRecipe.objects.create(
                ingredient_id=ingredient['id'],
                recipe=recipe,
                amount=ingredient['amount']
            )
        return recipe

    def update(self, instance, validated_data):
        ingredient_data = validated_data.pop('ingredients')
        IngredientInRecipe.objects.filter(recipe=instance).delete()

        for new_ingredient in ingredient_data:
            IngredientInRecipe.objects.create(
                ingredient=new_ingredient['id'],
                recipe=instance,
                amount=new_ingredient['amount']
            )
        instance.name = validated_data.pop('name')
        instance.text = validated_data.pop('text')
        instance.image = validated_data.pop('image')
        instance.cooking_time = validated_data.pop('cooking_time')
        instance.save()
        return instance

    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1
