from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import CreateAt, UpdateAt


class Gym(CreateAt, UpdateAt):
    athlete = models.ForeignKey('bodybuilders.BodyBuilding', on_delete=models.PROTECT, related_name='gyms')
    gym_name = models.CharField(unique=True, max_length=100)
    en_gym_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    number_of_machine = models.PositiveSmallIntegerField(_('Number of machine'))
    is_active = models.BooleanField(default=False)
    explain_gym = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.en_gym_name

    class Meta:
        db_table = 'gyms'
        verbose_name = _('gym')
        verbose_name_plural = _('gyms')


class GymTime(CreateAt, UpdateAt):
    gym = models.OneToOneField('Gym', on_delete=models.CASCADE, related_name='gym_time')
    male_opening_time = models.TimeField()
    male_closing_time = models.TimeField()
    explain_male_gym_time = models.TextField(help_text="Explain what days they can come to the club",
                                             blank=True, null=True)
    female_opening_time = models.TimeField()
    female_closing_time = models.TimeField()
    explain_female_gym_time = models.TextField(_('explain gym time'),
                                               help_text='Explain what days they can come to the club',
                                               blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.gym.gym_name

    class Meta:
        db_table = "gym_time"
        verbose_name = _('gym_time')
        verbose_name_plural = _('gym times')


class ContactGym(CreateAt, UpdateAt):
    gym = models.OneToOneField(Gym, on_delete=models.PROTECT, related_name='contact_us_gym')
    mobile_phone = models.CharField(_('mobile phone'), max_length=15, unique=True)
    landing_phone = models.CharField(_('landing phone'), max_length=15, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'gym_contact_us'
        verbose_name = _('gym contact us')
        verbose_name_plural = _('gym contact us')


class SocialNetworkClub(CreateAt, UpdateAt):
    gym = models.ForeignKey(Gym, on_delete=models.PROTECT, related_name='social_network_club')
    social_name = models.CharField(_('social name'), max_length=50)
    url_social = models.URLField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'social_contact_us'
        verbose_name = _('social contact us')
        verbose_name_plural = _('social contact us')
