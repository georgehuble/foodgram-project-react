from django.urls import path
from rest_framework import routers

from .views import TagsView, RecipeListView, \
    IngredientListView, IngredientDownloadView

router = routers.DefaultRouter()
router.register(r'tags',
                TagsView,
                basename='tags')
router.register(r'recipes',
                RecipeListView,
                basename='recipes')
router.register(r'ingredient',
                IngredientListView,
                basename='ingredient')

urlpatterns = router.urls

urlpatterns += [
    path('recipes/dowload_shopping_cart/', IngredientDownloadView)
]
