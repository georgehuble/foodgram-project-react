from rest_framework import routers

from .views import IngredientListView, RecipeListView, TagsView

router = routers.DefaultRouter()
router.register(r'tags',
                TagsView,
                basename='tags')
router.register(r'recipes',
                RecipeListView,
                basename='recipes')
# router.register(r'recipes',
#                 RecipeCreateView,
#                 basename='recipes')
router.register(r'ingredients',
                IngredientListView,
                basename='ingredients')

urlpatterns = router.urls
