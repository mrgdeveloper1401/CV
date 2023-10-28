from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_jalali.db import models as jmodels


class CreateModel(models.Model):
    created_at = jmodels.jDateTimeField(_('created_at'), auto_now_add=True)
    
    class Meta:
        abstract = True


class UpdateModel(models.Model):
    updated_at = jmodels.jDateTimeField(_('updated_at'), default=timezone.now)
    
    class Meta:
        abstract = True