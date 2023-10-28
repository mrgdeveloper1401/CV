from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CreateModel(models.Model):
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('created at')
        verbose_name_plural = _('created ats')
        db_table = 'create'
        abstract = True


class UpdateModel(models.Model):
    updated_at = models.DateTimeField(_('updated_at'), default=timezone.now)
    
    class Meta:
        verbose_name = _('update at')
        verbose_name_plural = _('update ats')
        db_table = 'update'
        abstract = True