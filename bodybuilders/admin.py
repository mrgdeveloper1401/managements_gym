from django.contrib import admin
from .models import BodyBuilding


@admin.register(BodyBuilding)
class BodyBuildingAdmin(admin.ModelAdmin):
    list_display = ('user', "height", "wight", "bmi", "is_active", "is_insurance")
    list_filter = ('is_active', 'is_insurance', 'created_at', 'updated_at')
    list_per_page = 20
    raw_id_fields = ('user',)
