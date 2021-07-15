from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'),
                              unique=True,
                              max_length=55,
                              blank=False)
    username = models.CharField(unique=True,
                                max_length=30,
                                blank=False)
    first_name = models.CharField(max_length=30,
                                  blank=False)
    last_name = models.CharField(max_length=30,
                                 blank=False)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Teg(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False,
                            verbose_name='Название')
    color = models.CharField(verbose_name=u'Color', max_length=7,
                             help_text=u'HEX color, as #RRGGBB',
                             unique=True, blank=False)
    slug = models.SlugField(max_length=50, unique=True, blank=False)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return f'{self.name}'


class Ingredient(models.Model):
    title = models.CharField(max_length=30, unique=True,
                             verbose_name='Наименование')
    amount = models.IntegerField(validators=[MinValueValidator(0)],
                                 verbose_name='Количество',
                                 null=True)
    dimension = models.CharField(max_length=30,
                                 verbose_name='Единица измерения')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.title}, {self.amount} {self.dimension}'


class Recipe(models.Model):
    author = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='recipe',
                               verbose_name='Автор')
    name = models.CharField(max_length=30,
                            verbose_name='Название')
    image = models.ImageField(upload_to='foodgram_api/',
                              blank=True,
                              verbose_name='Изображение')
    discription = models.TextField(max_length=250,
                                   verbose_name='Описание')
    ingredients = models.ManyToManyField(Ingredient,
                                         verbose_name='Ингредиенты')
    teg = models.ManyToManyField(Teg,
                                 verbose_name='Тег')
    time = models.IntegerField(verbose_name='Время приготовления',
                               help_text='Время в минутах',
                               validators=[MaxValueValidator(240),
                                           MinValueValidator(1)],
                               default=1)

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return f'{self.name}'
