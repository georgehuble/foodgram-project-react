from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_api.urls')),
    path('api/', include('recipe_api.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
    # path('api/users/', include('user_api.urls')),
    # path('api/users/<int:users_id>/', include('user_api.urls'))
]
