from django.db import models
from django.utils.translation import gettext_lazy as _
from django_jalali.db import models as jmodels


class CreateAt(models.Model):
    created_at = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _('Created At')
        verbose_name_plural = _('Created')


class UpdateAt(models.Model):
    updated_at = jmodels.jDateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        verbose_name = _('Updated At')
        verbose_name_plural = _('Updated')
