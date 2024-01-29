from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Users, UserNotification


@admin.register(Users)
class UsersAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", "mobile_phone")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "mobile_phone", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_superuser", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups", "is_superuser", "user_permissions")
    search_fields = ("username", "first_name", "last_name", "email", "mobile_phone")
    ordering = ("username",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
    list_editable = ('is_staff', 'is_superuser', 'is_active')


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ('user', "title_notification", "created_at", "is_published")
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    list_per_page = 20
    raw_id_fields = ('user',)
