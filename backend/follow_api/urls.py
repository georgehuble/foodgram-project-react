from django.urls import path

from .utils import download_shopping_cart
from .views import FavouriteView, ShoppingView, SubscribeView

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
