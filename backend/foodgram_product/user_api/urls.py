from django.urls import path, include

from .views import UsersViewSet, UserDetailViewSet
from follow_api.views import SubscribeView

urlpatterns = [
    path('users/', UsersViewSet.as_view({'get': 'list'}),
         name='users'),
    path('users/subscriptions/', SubscribeView,
         name='subscribers'),
    path('users/<id>/', UserDetailViewSet.as_view({'get': 'list'}),
         name='users_profile'),
    path('users/<id>/subscribe/',
         SubscribeView.as_view({'get': 'retrieve',
                                'delete': 'destroy'}),
         name='subscribe')
]
