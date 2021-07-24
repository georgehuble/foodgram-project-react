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
from django.http import HttpResponse, Http404


class MixinsViewSet(mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    pass


class FavouriteView(MixinsViewSet):
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

    def delete(self):
        favourite_id = Favourite.kwargs.get('favourite_id')
        favourite = Favourite.objects.filter(favourite=favourite_id)
        return favourite
