from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import DeliveryMethod


class DeliveryMethodForm(forms.ModelForm):

    class Meta:
        model = DeliveryMethod
        fields = ['name', 'cost', 'friendly_name']
