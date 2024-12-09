from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import AppUserManager

class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)

    objects = AppUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    PASSWORD_FIELD = 'password'

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    experience = models.IntegerField(help_text="Years of experience")

    def __str__(self):
        return self.name


def populate_artists():
    if not Artist.objects.exists():
        Artist.objects.bulk_create([
            Artist(name="Alice", bio="Specializes in abstract art.", experience=5),
            Artist(name="Bob", bio="Expert in realistic portraits.", experience=7),
            Artist(name="Charlie", bio="Focused on modern digital design.", experience=4),
        ])
