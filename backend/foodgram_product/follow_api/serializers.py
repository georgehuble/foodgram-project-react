from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import ReadOnlyField
from recipe_api.models import Recipe

from .models import Favourite
from recipe_api.serializers import RecipeSerializer


class FavouriteSerializer(serializers.ModelSerializer):
    image = RecipeSerializer(many=False, read_only=True)

    class Meta:
        model = Favourite
        fields = ('id', 'name', 'image')

    def to_representation(self, instance):
        rep = super(FavouriteSerializer, self).to_representation(instance)
        rep['name'] = instance.name.name
        return rep
