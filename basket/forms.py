from django import forms

from .models import DeliveryMethod


class DeliveryMethodForm(forms.ModelForm):

    class Meta:
        model = DeliveryMethod
        fields = ['name', 'cost', 'friendly_name']
