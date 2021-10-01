from django.urls import path

from follow_api.views import SubscribeListView

from .views import UserViewSet

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list'}),
         name='users'),
    path('users/subscriptions/', SubscribeListView.as_view({'get': 'list'}),
         name='subscriptions'),
]
