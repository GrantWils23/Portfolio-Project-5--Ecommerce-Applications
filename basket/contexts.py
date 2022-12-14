from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):
    basket_items = []
    total = 0
    product_count = 0
    delivery = request.session.get('deliveryfee', 3.5)
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
