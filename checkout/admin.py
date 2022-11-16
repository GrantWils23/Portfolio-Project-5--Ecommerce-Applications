from django.contrib import admin
from .models import Order, OrderLineItem, DeliveryMethod


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_method', 'order_total', 'grand_total')
    fields = ('order_number', 'full_name', 'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1', 'street_address2',
              'county', 'date', 'delivery_method', 'order_total',
              'grand_total')
    list_display = ('order_number', 'date', 'full_name', 'delivery_method',
                    'order_total', 'grand_total')
    ordering = ('-date',)


class DeliveryMethodAdmin(admin.ModelAdmin):
    list_display = ('delivery_method_name', 'delivery_method_cost')


admin.site.register(Order, OrderAdmin)
admin.site.register(DeliveryMethod, DeliveryMethodAdmin)
