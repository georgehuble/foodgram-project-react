from colorfield.fields import ColorField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import UniqueConstraint

from user_api.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=False,
                            verbose_name='Название')
    color = ColorField(verbose_name=u'Color', max_length=7,
                       help_text=u'HEX color, as #RRGGBB',
                       blank=True)
    slug = models.SlugField(max_length=50, unique=True,
                            blank=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True,
                            verbose_name='Наименование',
                            blank=False)
    amount = models.IntegerField(validators=[MinValueValidator(0)],
                                 verbose_name='Количество',
                                 blank=False)
    measurement_unit = models.CharField(max_length=30,
                                        verbose_name='Единица измерения',
                                        blank=False)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.amount} {self.measurement_unit}'


class Recipe(models.Model):
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='recipes',
                               verbose_name='Автор',
                               blank=False)
    name = models.CharField(max_length=30,
                            verbose_name='Название',
                            blank=False)
    image = models.ImageField(upload_to='user_api/',
                              blank=False,
                              verbose_name='Изображение')
    text = models.TextField(max_length=250,
                            verbose_name='Описание',
                            blank=False)
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингредиенты',
                                         blank=False)
    teg = models.ManyToManyField(Tag,
                                 verbose_name='Тег',
                                 blank=False)
    cooking_time = models.IntegerField(verbose_name='Время приготовления',
                                       help_text='Время в минутах',
                                       validators=[MaxValueValidator(240),
                                                   MinValueValidator(1)],
                                       default=1,
                                       blank=False)
    favourites = models.ManyToManyField(CustomUser, related_name='favourite',
                                        default=None, blank=True)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.name}'


class Shopping(models.Model):
    name = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             verbose_name='Название рецепта')

    class Meta:
        # UniqueConstraint(fields=['author', 'name'], name='favorite')
        # unique_together = ('author', 'name')
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Список покупок'

    def __str__(self):
        return f'{self.name}'
