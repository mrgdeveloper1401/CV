from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CreateModel(models.Model):
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    
    class Meta:
        abstract = True


class UpdateModel(models.Model):
    updated_at = models.DateTimeField(_('updated_at'), default=timezone.now)
    
    class Meta:
        abstract = True