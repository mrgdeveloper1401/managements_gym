from django.contrib import admin
from .models import Coach, Skill


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ('athles', 'is_active', "created_at", "updated_at", "result_coaching_card")
    list_filter = ('is_active', 'created_at', 'updated_at')
    list_editable = ('is_active',)
    search_fields = ('athles',)
    list_per_page = 20
    date_hierarchy = 'created_at'
    raw_id_fields = ('athles',)
    filter_horizontal = ('skill', 'gym')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'created_at', 'updated_at', 'is_active')
    list_editable = ('is_active',)
    search_fields = ('skill_name',)
    date_hierarchy = 'created_at'
    list_per_page = 20
    list_filter = ('created_at', 'updated_at', 'is_active')
