from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# import app django
from core.models import CreateAt, UpdateAt
from .managers import UsersManager


class Users(AbstractUser):
    email = models.EmailField(unique=True, max_length=254, blank=True)
    mobile_phone = models.CharField(max_length=15, unique=True)

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
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='notifications')
    title_notification = models.CharField(max_length=254)
    body_notification = models.TextField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user} -- {self.created_at}'

    class Meta:
        db_table = 'user_notifications'
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

