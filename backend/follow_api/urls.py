from django.urls import path

from .views import FavouriteView, ShoppingView, SubscribeView
from user_api.views import UserViewSet

urlpatterns = [
    path('users/<id>/',
         UserViewSet.as_view({'get': 'retrieve'}),
         name='user'),
    path('users/<id>/subscribe/',
         SubscribeView.as_view({'get': 'retrieve',
                                'delete': 'destroy'}),
         name='subscribe'),
    path('recipes/<id>/favorite/',
         FavouriteView.as_view({'get': 'retrieve',
                                'delete': 'destroy'})),
    path('recipes/<id>/shopping_cart/',
         ShoppingView.as_view({'get': 'retrieve',
                               'delete': 'destroy'})),
]
