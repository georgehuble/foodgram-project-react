from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.serializers import ReadOnlyField
from recipe_api.models import Recipe

from .models import Favourite


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ('id', 'name')

    def to_representation(self, instance):
        rep = super(FavouriteSerializer, self).to_representation(instance)
        rep['name'] = instance.name.name
        return rep
