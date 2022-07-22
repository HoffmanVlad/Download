from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import BooleanField, CharField, FloatField, SlugField
import jwt
from datetime import datetime
from datetime import timedelta
from django.conf import settings
from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

USER_MODEL = settings.AUTH_USER_MODEL

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('Указанное имя пользователя должно быть установлено')

        if not email:
            raise ValueError('Данный адрес электронной почты должен быть установлен')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.validate_email], unique=True, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = UserManager()

    def __str__(self):
        return f'{self.username} {self.email}'
    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        # token = jwt.encode({'id': self.pk, 'exp': int(dt.strftime('%s')) }, settings.SECRET_KEY, algorithm='HS256')
        token = jwt.encode({
             'id': self.pk,
             'exp': dt.utcfromtimestamp(dt.timestamp())    #CHANGE HERE
    }, settings.SECRET_KEY, algorithm='HS256')
        return token

class Watch(models.Model):
    name_model = models.CharField(max_length=50)
    model_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    color = models.CharField(max_length=20)
    cm = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name_model} {self.model_price} {self.cm}'


    
class Phone(models.Model):
    name_model = models.CharField(max_length=100)
    model_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    color = models.CharField(max_length=20)
    diagonal = models.PositiveIntegerField()
    wifi = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name_model} {self.model_price} {self.color}'