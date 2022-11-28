from django.contrib import admin
from .models import WeaponSystem, WeaponPlatform, CamoPattern
from .models import TechService, PaintService

# Register your models here.


class WeaponSystemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'base_price',
    )


class WeaponPlatformAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'base_price',
    )


class CamoPatternAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'base_price',
    )


class TechServiceAdmin(admin.ModelAdmin):
    list_display = (
        'quote_number',
        'user_profile',
        'full_name',
        'email',
        'phone_number',
        'weapon_platform',
        'weapon_system',
        'additional_info',
        'image',
    )

    search_fields = ['quote_number', 'full_name']


class PaintServiceAdmin(admin.ModelAdmin):
    list_display = (
        'quote_number',
        'user_profile',
        'full_name',
        'email',
        'phone_number',
        'camo_pattern',
        'weapon_system',
        'additional_info',
        'image',
    )

    search_fields = ['quote_number', 'full_name']


admin.site.register(WeaponSystem, WeaponSystemAdmin)
admin.site.register(WeaponPlatform, WeaponPlatformAdmin)
admin.site.register(CamoPattern, CamoPatternAdmin)
admin.site.register(TechService, TechServiceAdmin)
admin.site.register(PaintService, PaintServiceAdmin)
