from django.urls import path
from rest_framework import routers

from .utils import download_shopping_cart
from .views import IngredientListView, RecipeListView, TagsView

router = routers.DefaultRouter()
router.register(r'tags',
                TagsView,
                basename='tags')
router.register(r'recipes',
                RecipeListView,
                basename='recipes')
router.register(r'ingredients',
                IngredientListView,
                basename='ingredients')

urlpatterns = [
    path('recipes/download_shopping_cart/',
         download_shopping_cart),
]

urlpatterns += router.urls
