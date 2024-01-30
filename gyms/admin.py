from django.contrib import admin
from .models import GymTime, ContactGym, SocialNetworkClub, Gym


class SocialGymInline(admin.StackedInline):
    model = SocialNetworkClub
    extra = 0


class GymTimeInline(admin.StackedInline):
    model = GymTime
    extra = 0


class ContactGymInline(admin.StackedInline):
    model = ContactGym
    extra = 0


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_display = ('athlete', 'gym_name', "en_gym_name", 'number_of_machine', "is_active")
    list_editable = ('is_active',)
    search_fields = ('gym_name', "en_gym_name", "athlete")
    date_hierarchy = 'created_at'
    list_per_page = 20
    raw_id_fields = ('athlete',)
    prepopulated_fields = {'slug': ('en_gym_name',)}
    inlines = (SocialGymInline, GymTimeInline, ContactGymInline)
    fieldsets = (
        ('add gym', {'fields': ('athlete', 'gym_name', 'en_gym_name', 'slug', 'number_of_machine'), }),
        ('result signup gym', {'fields': ('is_active', 'explain_gym'), }),
    )


@admin.register(GymTime)
class GymTimeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    list_display = ('gym', 'male_opening_time', 'male_closing_time', 'female_opening_time', 'female_closing_time',
                    "is_active", 'created_at', 'updated_at')


@admin.register(ContactGym)
class ContactGymAdmin(admin.ModelAdmin):
    list_display = ('gym', "mobile_phone", "email", "landing_phone", "is_active")
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_per_page = 20
    search_fields = ('gym', 'mobile_phone', 'email', 'landing_phone')


@admin.register(SocialNetworkClub)
class SocialNetworkClubAdmin(admin.ModelAdmin):
    list_display = ('gym', 'social_name', 'url_social', "is_active")
    list_editable = ('is_active',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_per_page = 20
