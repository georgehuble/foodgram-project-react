from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from drf_extra_fields.fields import Base64ImageField
from user_api.models import CustomUser


class Tag(models.Model):
    name = models.CharField(
        max_length=30, blank=False,
        verbose_name='Название')
    color = ColorField(
        verbose_name=u'Color', max_length=7,
        help_text=u'HEX color, as #RRGGBB',
        blank=True)
    slug = models.SlugField(
        max_length=50, unique=True,
        blank=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name='Название ингредиента',
        max_length=200,
        help_text='Укажите название ингредиента',
    )
    measurement_unit = models.CharField(
        verbose_name='Единица измерения',
        max_length=200,
        help_text='Укажите единицу измерения'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор',
        blank=False)
    name = models.CharField(
        max_length=30,
        verbose_name='Название',
        blank=False)
    image = Base64ImageField(
        upload_to='user_api/',
        blank=False,
        verbose_name='Изображение')
    text = models.TextField(
        max_length=250,
        verbose_name='Описание',
        blank=False)
    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='ingredients',
        through='IngredientInRecipe',
        verbose_name='Ингредиенты',
        blank=False)
    tags = models.ManyToManyField(
        Tag,
        related_name='tags',
        verbose_name='Теги',
        blank=False)
    cooking_time = models.IntegerField(
        verbose_name='Время приготовления',
        help_text='Время в минутах',
        validators=[MaxValueValidator(240),
                    MinValueValidator(1)],
        default=1,
        blank=False)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.name}'


class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        verbose_name='Ингредиент в рецепте')
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт')
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество ингредиентов',
        default=1,
        validators=[MinValueValidator(1), ])

    class Meta:
        verbose_name = 'Количество ингредиента в рецепте'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.ingredient} в {self.recipe}'
