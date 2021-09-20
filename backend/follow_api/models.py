from django.db import models
from django.db.models import UniqueConstraint
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
        verbose_name = 'избранное'
        verbose_name_plural = 'Избранное'

    def __str__(self):
        return f'{self.name}'


class Subscribe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             related_name='subscriber',
                             verbose_name='Подписчик')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                               related_name='following',
                               verbose_name='Автор')

    class Meta:
        UniqueConstraint(fields=['author', 'user'], name='unique_together')
        unique_together = ('author', 'user')
        verbose_name = 'подписки'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.author.username


class Shopping(models.Model):
    name = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             verbose_name='Название рецепта')

    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')

    class Meta:
        unique_together = ('name', 'user')
        verbose_name = 'покупки'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f'{self.name}'
