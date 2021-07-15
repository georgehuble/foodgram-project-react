from django.contrib.auth import get_user_model
from django.core.mail import send_mail, mail_admins
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import Teg, Ingredient, Recipe

User = get_user_model()


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'id', 'username', 'password',
                  'first_name', 'last_name')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('email', 'username',
                  'first_name', 'last_name')
        model = User


class TegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teg
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'


class TokenObtainPairNoPasswordSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        attrs.update({'password': ''})
        data = super(TokenObtainPairNoPasswordSerializer,
                     self).validate(attrs)
        user = User.objects.get(email=self.context['request'].data.get('email')
                                )
        data = data["refresh"]
        send_mail(
            'Ваш confirmation_code',
            f'Ваш confirmation_code {data}.',
            mail_admins,
            [user.email],
            fail_silently=False,
        )
        return {'message': 'Вам отправлено письмо с confirmation_code'}


class TokenRefreshNoPassworSerializer(TokenRefreshSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['refresh'].required = False

    def validate(self, attrs):
        attrs.update({'refresh':
                      self.context['request'].data.get('confirmation_code')})
        return super().validate(attrs)
