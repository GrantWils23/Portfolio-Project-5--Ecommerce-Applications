import django_filters
from django.forms.widgets import TextInput

from checkout.models import Order
from services.models import CamoPattern, PaintService, TechService


class OrdersFilter(django_filters.FilterSet):
    date__gt = django_filters.DateFilter(field_name='date', lookup_expr 
    ='gte', label='Start Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    date__lt = django_filters.DateFilter(field_name='date', lookup_expr 
    = 'lte', label='End Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = Order
        fields = {'user_profile': ['exact'],
                  'full_name': ['icontains'],
                  'email': ['exact'],
                  'date': ['gt', 'lt'],
                  'order_number': ['icontains'],
                  }


class PaintQuoteFilter(django_filters.FilterSet):
    date__gt = django_filters.DateFilter(field_name='date', lookup_expr 
    ='gte', label='Start Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    date__lt = django_filters.DateFilter(field_name='date', lookup_expr 
    = 'lte', label='End Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = PaintService
        fields = {'user_profile': ['exact'],
                  'full_name': ['icontains'],
                  'email': ['exact'],
                  'date': ['gt', 'lt'],
                  'quote_number': ['icontains'],
                  }


class TechQuoteFilter(django_filters.FilterSet):
    date__gt = django_filters.DateFilter(field_name='date', lookup_expr 
    ='gte', label='Start Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))
    date__lt = django_filters.DateFilter(field_name='date', lookup_expr 
    = 'lte', label='End Date', widget=TextInput(attrs={'placeholder': 'yyyy-mm-dd'}))

    class Meta:
        model = TechService
        fields = {'user_profile': ['exact'],
                  'full_name': ['icontains'],
                  'email': ['exact'],
                  'date': ['gt', 'lt'],
                  'quote_number': ['icontains'],
                  }
