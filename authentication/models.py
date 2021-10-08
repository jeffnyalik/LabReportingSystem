from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('User should have a username')
        if not email:
            raise ValueError('User should have an email address')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise ValueError('User should have a password')
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email  = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
   
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_facility_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


    def __str__(self):
        return self.email


class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_user')
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='customuser_profile')
    image = models.ImageField(upload_to='images/profile//%Y/%m/%d', blank=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username