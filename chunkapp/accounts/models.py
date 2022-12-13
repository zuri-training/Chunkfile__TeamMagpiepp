from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators

# Create your models here

class chunkappManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        user = self._create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class chunkapp(AbstractBaseUser, PermissionsMixin):
    username=None
    id = models.BigAutoField(primary_key = True)
    email = models.EmailField(validators = [validators.EmailValidator()], unique=True, max_length = 250)
    fullname = models.CharField(max_length=250, blank=True)
    password = models.CharField( max_length=250, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = chunkappManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'fullname']

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

