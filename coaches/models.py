from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UpdateAt, CreateAt


class Coach(CreateAt, UpdateAt):
    athles = models.OneToOneField('bodybuilders.BodyBuilding', on_delete=models.PROTECT, related_name='coach')
    gym = models.ManyToManyField('gyms.Gym', related_name='coach')
    skill = models.ManyToManyField('Skill', related_name='coach_skills')
    coaching_card = models.ImageField(upload_to='coaches/%y/%m/%d')
    education_image = models.ImageField(upload_to='coaches/education/%Y/%m/%d')
    alter_coaching_card = models.CharField(max_length=50, blank=True, null=True)
    result_coaching_card = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.athles

    class Meta:
        db_table = 'coach'
        verbose_name = _('Coach')
        verbose_name_plural = _('Coach')


class Skill(CreateAt, UpdateAt):
    skill_name = models.CharField(max_length=50, unique=True)
    description_skill = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.skill_name

    class Meta:
        db_table = 'skill'
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
