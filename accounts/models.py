from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import CreateModel
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels
from django.utils import timezone
from .manager import UsersManager


class MobilePreCode(models.Model):
    precode = models.CharField(_('precode'), max_length=5)
    
    def __str__(self) -> str:
        return self.precode
    
    class Meta:
        verbose_name = _('mobile precode')
        verbose_name_plural = _('mobile precodes')
        db_table = 'precode'

class User(AbstractBaseUser, PermissionsMixin, CreateModel):
    full_name = models.CharField(_('Full name'), max_length=100)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    precde = models.ForeignKey(MobilePreCode, on_delete=models.PROTECT, related_name='codes', blank=True, null=True)
    mobile_phone = models.CharField(_('Mobile phone'), max_length=11, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = jmodels.jDateTimeField(_("last login"), default=timezone.now())

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