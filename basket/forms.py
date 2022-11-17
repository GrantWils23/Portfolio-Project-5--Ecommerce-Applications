from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import DeliveryMethod


class DeliveryMethodForm(forms.ModelForm):

    class Meta:
        ''' meta data for the admin booking form '''
        model = DeliveryMethod
        fields = ['delivery_method_name', 'delivery_method_cost']
