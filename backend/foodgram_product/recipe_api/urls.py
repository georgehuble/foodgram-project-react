from django.urls import path
from rest_framework import routers

from .views import TagsView, RecipeListView, IngredientListView
from follow_api.views import FavoriteView

router = routers.SimpleRouter()
router.register(r'tags', TagsView, basename='tags')
router.register(r'recipes', RecipeListView, basename='recipes')
# router.register(r'recipes/(?P<recipes_id>\d+)/favorite',
#                 FavoriteView,
#                 basename='favorite')
router.register(r'ingredient', IngredientListView, basename='ingredient')

urlpatterns = router.urls

urlpatterns += [
    path('recipes/<pk>/favorite/',
         FavoriteView.as_view())
]
