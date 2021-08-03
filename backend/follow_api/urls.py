from django.urls import path

from .views import (FavouriteView, ShoppingView, SubscribeView,
                    download_shopping_cart)

urlpatterns = [
    path('users/<id>/subscribe/',
         SubscribeView.as_view({'get': 'retrieve',
                                'delete': 'destroy'}),
         name='subscribe'),
    path('download_shopping_cart/',
         download_shopping_cart),
    path('recipes/<id>/favorite/',
         FavouriteView.as_view({'get': 'retrieve',
                                'delete': 'destroy'})),
    path('recipes/<id>/shopping_cart/',
         ShoppingView.as_view({'get': 'retrieve',
                               'delete': 'destroy'})),
    path('recipes/<id>/shopping_cart/',
         ShoppingView.as_view({'get': 'retrieve',
                               'delete': 'destroy'}))
]
