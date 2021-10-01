from rest_framework import serializers

from recipe_api.models import Recipe
from user_api.models import CustomUser

from .models import Subscribe


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name', 'image', 'cooking_time')


class SubscribeSerializer(serializers.ModelSerializer):
    recipes = FavouriteSerializer(many=True, read_only=True)
    is_subscribed = serializers.SerializerMethodField('check_subscription')
    recipes_count = serializers.SerializerMethodField('check_recipes_count')

    def check_subscription(self, obj):
        user = self.context.get('request').user
        return Subscribe.objects.filter(user=obj, author=user).exists()

    def check_recipes_count(self, obj):
        return Recipe.objects.filter(author=obj).count()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username',
                  'first_name', 'last_name',
                  'is_subscribed', 'recipes',
                  'recipes_count',)
