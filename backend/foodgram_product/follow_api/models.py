from django.db import models

from recipe_api.models import Recipe
from user_api.models import CustomUser


class Favorite(models.Model):
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='recipes')
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             related_name='user')

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.recipe}'
