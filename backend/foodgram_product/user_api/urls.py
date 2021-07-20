from django.urls import path, include

from .views import UsersViewSet, UserDetailViewSet


urlpatterns = [
    path('users/', UsersViewSet.as_view({'get': 'list'}), name='users'),
    path('users/<id>/', UserDetailViewSet.as_view({'get': 'list'}), name='users_profile')
]
