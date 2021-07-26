from django.db import models

from recipe_api.models import Recipe
from user_api.models import CustomUser


class Favourite(models.Model):
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    name = models.ForeignKey(Recipe,
                             on_delete=models.CASCADE,
                             related_name='favourites',
                             verbose_name='Наименование рецепта')

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.name}'
