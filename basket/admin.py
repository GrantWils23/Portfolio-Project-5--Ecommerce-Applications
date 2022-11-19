from django.contrib import admin
from .models import DeliveryMethod


class DeliveryMethodAdmin(admin.ModelAdmin):
    """ Delivery Method Information admin panel """
    list_display = ('name', 'cost', 'friendly_name')


admin.site.register(DeliveryMethod, DeliveryMethodAdmin)
