from django import forms
from .models import WeaponSystem, WeaponPlatform, CamoPattern
from .models import PaintService, TechService


class PaintServiceForm(forms.ModelForm):

    full_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-group col-12 col-sm-8 col-md-6 col-lg-4"}))
    weapon_system = forms.ModelChoiceField(WeaponSystem.objects.all(), widget=forms.RadioSelect())

    class Meta:
        model = PaintService
        fields = ('full_name', 'email', 'phone_number',
                  'camo_pattern', 'weapon_system',
                  'additional_info', 'image',)
        widgets = {'weapon_system': forms.RadioSelect()}

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     weaponsystems = WeaponSystem.objects.all()
    #     ws_friendly_names = [(ws.id, ws.get_friendly_name()) for ws in weaponsystems]
    #     camopatterns = CamoPattern.objects.all()
    #     cp_friendly_names = [(cp.id, cp.get_friendly_name()) for cp in camopatterns]

    #     # self.fields['weapon_system'].widget = forms.RadioSelect
    #     self.fields['weapon_system'].choices = ws_friendly_names
    #     self.fields['camo_pattern'].choices = cp_friendly_names
    #     for field_name, field in self.fields.items():
    #         field.widget.attrs['class'] = 'text-secondary'


class TechServiceForm(forms.ModelForm):

    class Meta:
        model = TechService
        fields = ('full_name', 'email', 'phone_number',
                  'weapon_platform', 'weapon_system',
                  'additional_info', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        weaponplatforms = WeaponPlatform.objects.all()
        wp_friendly_names = [(wp.id, wp.get_friendly_name()) for wp in weaponplatforms]
        weaponsystems = WeaponSystem.objects.all()
        ws_friendly_names = [(ws.id, ws.get_friendly_name()) for ws in weaponsystems]

        self.fields['weapon_platform'].choices = wp_friendly_names
        self.fields['weapon_system'].choices = ws_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-secondary'

