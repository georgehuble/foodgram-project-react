from django.core.validators import MinValueValidator
from drf_extra_fields.fields import Base64ImageField
from follow_api.models import Favourite
from recipe_api.models import Shopping
from rest_framework import serializers
from rest_framework.serializers import ReadOnlyField
from user_api.serializers import UserSerializer

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
    name = ReadOnlyField(source='ingredient.name')
    measurement_unit = ReadOnlyField(source='ingredient.measurement_unit')
    amount = serializers.IntegerField(
        validators=[
            MinValueValidator(
                1,
                'Убедитесь, что количество ингредиента больше или равно 1'
            )
        ]
    )

    class Meta:
        model = IngredientInRecipe
        fields = ['id', 'name', 'measurement_unit', 'amount']


class RecipeSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    image = Base64ImageField(max_length=None, use_url=True)
    cooking_time = serializers.IntegerField(
        validators=[
            MinValueValidator(
                1,
                'Убедитесь, что время приготовления не менее 1'
            )
        ]
    )
    is_favorited = serializers.SerializerMethodField('check_if_is_favorited')
    is_in_shopping_cart = serializers.SerializerMethodField('check_if_is_in_shopping_cart')

    def check_if_is_favorited(self, obj):
        user = self.context.get('request').user
        try:
            return Favourite.objects.filter(user=user, name=obj).exists()
        except TypeError:
            return Favourite.objects.filter(name=obj).exists()

    def check_if_is_in_shopping_cart(self, obj):
        user = self.context.get('request').user
        try:
            return Shopping.objects.filter(user=user, name=obj).exists()
        except TypeError:
            return Shopping.objects.filter(name=obj).exists()

    def create(self, validated_data):
        ingredients = self.context['request'].data['ingredients']
        tags = validated_data.pop('tags')
        recipe = Recipe.objects.create(**validated_data)
        recipe.tags.set(tags)
        for ingredient in ingredients:
            IngredientInRecipe.objects.create(
                recipe=recipe,
                ingredient_id=ingredient['id'],
                amount=ingredient['amount']
            )
        return recipe

    def update(self, recipe, validated_data):
        recipe.name = validated_data.get('name', recipe.name)
        recipe.text = validated_data.get('text', recipe.text)
        recipe.image = validated_data.get('image', recipe.image)
        recipe.cooking_time = validated_data.get('cooking_time', recipe.cooking_time)
        if 'ingredient' in self.initial_data:
            ingredients = validated_data.pop('ingredients')
            recipe.ingredients.clear()
            ingredients(ingredients, recipe)
        if 'tags' in self.initial_data:
            tags_data = validated_data.pop('tags')
            recipe.tags.set(tags_data)
            recipe.save()
        return recipe


    class Meta:
        model = Recipe
        fields = '__all__'
        depth = 1

    def __init__(self, *args, **kwargs):
        super(RecipeSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].method in ['POST']:
                self.fields['ingredients'] = AddIngredientToRecipeSerializer(
                    source='ingredientinrecipe',
                    many=True)
                self.fields['tags'] = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
            elif self.context['request'].method in ['PATCH']:
                self.fields['tags'] = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
            else:
                self.fields['ingredients'] = AddIngredientToRecipeSerializer(
                    source='ingredientinrecipe_set',
                    many=True)
        except KeyError:
            pass
