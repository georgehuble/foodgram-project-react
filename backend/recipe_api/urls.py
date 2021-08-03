from rest_framework import routers

from .views import IngredientListView, RecipeListView, TagsView

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
