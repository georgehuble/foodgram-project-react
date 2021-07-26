from urllib import request
from rest_framework.decorators import api_view
from rest_framework import generics, permissions, views, response, status, mixins, viewsets
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Favourite
from .serializers import FavouriteSerializer
from recipe_api.models import Recipe
from user_api.models import CustomUser
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend


class FavouriteView(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FavouriteSerializer
    filter_backends = (DjangoFilterBackend,)
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        data = {
            'user': request.user.pk,
            'name': self.kwargs.get('id')
        }
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            self.perform_create(serializer)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, pk=None):
        if Favourite.objects.filter(name=request.user.pk).exists():
            Favourite.objects.get(user=request.user.pk, name=self.kwargs.get('id')).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
