from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    basket_items = 0
    total = 0
    product_count = 0
    delivery = 0
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
