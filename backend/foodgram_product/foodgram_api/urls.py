from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import (TokenRefreshNoPasswordView,
                    TokenObtainPairNoPasswordView,
                    UsersViewSet)

router = DefaultRouter()
router.register('users', UsersViewSet,
                basename='users')

token_urlpatterns = [
    path('token/', TokenRefreshNoPasswordView.as_view(),
         name='token_obtain_pair'),
    path('email/', TokenObtainPairNoPasswordView.as_view(),
         name='token_request_pair'),
]

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(token_urlpatterns)),
]
