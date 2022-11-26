from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from .models import DeliveryMethod
from checkout.models import Order
from checkout.forms import OrderForm


def basket_contents(request):
    delmeth = DeliveryMethod.objects.get(pk=1)  # default shipping method
    basket_items = []
    total = 0
    product_count = 0
    delivery = request.session.get('deliveryfee', delmeth.cost)
    basket = request.session.get('basket', {})
    grand_total = 0
    delivery_id = request.session.get('delivery_id')

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if product_count == 0:
        delivery = 0
    else:
        grand_total = Decimal(delivery) + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'deliveryfee': delivery,
        'delivery_id': delivery_id,
        'grand_total': grand_total,
    }

    return context
