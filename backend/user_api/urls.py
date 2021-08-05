from django.urls import path
from follow_api.views import SubscribeListView

from .views import UserDetailViewSet, UsersViewSet

urlpatterns = [
    path('users/', UsersViewSet.as_view({'get': 'list'}),
         name='users'),
    path('users/subscriptions/', SubscribeListView.as_view({'get': 'list'}),
         name='subscriptions'),
    path('users/<id>/', UserDetailViewSet.as_view({'get': 'list'}),
         name='users_profile')
]
