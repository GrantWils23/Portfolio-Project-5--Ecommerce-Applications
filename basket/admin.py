from django.contrib import admin
from .models import DeliveryMethod


class DeliveryMethodAdmin(admin.ModelAdmin):
    """ Delivery Method Information admin panel """
    list_display = ('delivery_method_name', 'delivery_method_cost')


admin.site.register(DeliveryMethod, DeliveryMethodAdmin)
