from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import CreateModel, UpdateModel
from django.utils.translation import gettext_lazy as _
from .manager import UsersManager


class User(AbstractBaseUser, PermissionsMixin, CreateModel, UpdateModel):
    full_name = models.CharField(_('Full name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    mobile_phone = models.CharField(_('Mobile phone'), max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    objects = UsersManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name', 'mobile_phone')
    
    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True
    
    @property
    def is_admin(self):
        return self.is_staff