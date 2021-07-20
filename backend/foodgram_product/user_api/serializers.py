from django.core.mail import send_mail, mail_admins
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from .models import CustomUser


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = CustomUser
        fields = ('email', 'id', 'username', 'password',
                  'first_name', 'last_name')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',
                  'first_name', 'last_name')


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',
                  'first_name', 'last_name',
                  'is_subscribed')


class UserMeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'username',
                  'first_name', 'last_name',
                  'is_subscribed')


class TokenObtainPairNoPasswordSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def validate(self, attrs):
        attrs.update({'password': ''})
        data = super(TokenObtainPairNoPasswordSerializer,
                     self).validate(attrs)
        user = CustomUser.objects.get(email=self.context['request'].data.get('email')
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


class TokenRefreshNoPasswordSerializer(TokenRefreshSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['refresh'].required = False

    def validate(self, attrs):
        attrs.update({'refresh':
                      self.context['request'].data.get('confirmation_code')})
        return super().validate(attrs)
