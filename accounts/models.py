from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# import app django
from core.models import CreateAt, UpdateAt
from .managers import UsersManager


class Users(AbstractUser):
    email = models.EmailField(_('email'), unique=True, max_length=254, blank=True)
    mobile_phone = models.CharField(_('mobile phone'), max_length=15, unique=True)

    objects = UsersManager()

    def __str__(self):
        return f'{self.email} -- {self.mobile_phone} -- {self.username}'

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'mobile_phone', 'first_name', 'last_name')

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')


class UserNotification(CreateAt):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications', verbose_name=_('user'))
    title_notification = models.CharField(_('title notification'), max_length=254)
    body_notification = models.TextField(_('body notification'))
    is_published = models.BooleanField(_('publish'), default=True)

    def __str__(self):
        return f'{self.user} -- {self.created_at}'

    class Meta:
        db_table = 'user_notifications'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

