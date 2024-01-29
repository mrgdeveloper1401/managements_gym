from django.db import models
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from core.models import CreateAt, UpdateAt


class BodyBuilding(CreateAt, UpdateAt):
    class GenderChoices(models.TextChoices):
        male = 'male',
        female = 'female'

    user = models.OneToOneField('accounts.Users', on_delete=models.PROTECT, related_name="body_building")
    gender = models.CharField(max_length=6, choices=GenderChoices.choices, default=GenderChoices.male)
    height = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)
    wight = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    birth_day = jmodels.jDateField()
    nation_code = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_insurance = models.BooleanField(default=False)

    @property
    def bmi(self):
        w = self.wight
        h = self.height
        bmi = w / (pow(h,2))
        return bmi

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'body_building'
        verbose_name = _('Body Building')
        verbose_name_plural = _('Body Buildings')

