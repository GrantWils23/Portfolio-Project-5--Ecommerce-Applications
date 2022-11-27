from django import forms
from .models import WeaponSystem, WeaponPlatform, CamoPattern
from .models import PaintService, TechService


class PaintServiceForm(forms.ModelForm):

    class Meta:
        model = PaintService
        fields = ('full_name', 'user_profile', 'email', 'phone_number',
                  'camo_pattern', 'weapon_system',
                  'additional_info', 'image',)


class TechServiceForm(forms.ModelForm):

    class Meta:
        model = TechService
        fields = ('full_name', 'user_profile', 'email', 'phone_number',
                  'weapon_platform', 'weapon_system',
                  'additional_info', 'image',)
