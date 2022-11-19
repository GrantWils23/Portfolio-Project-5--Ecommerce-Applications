from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from basket.models import DeliveryMethod


from .forms import OrderForm
from .models import Order


def checkout(request):
    """ The view that returns the checkout page """
    delivery_id = request.session.get('delivery_id')  # del_id from context.py
    delivery_method = get_object_or_404(DeliveryMethod, pk=delivery_id)
    print(delivery_id)
    print(delivery_method)

    initial_data = {
        'delivery': delivery_id,
    }

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm(initial=initial_data)
    template = 'checkout/checkout.html'
    context = {
        'delivery_method': delivery_method,
        'order_form': order_form,
        'delivery_id': delivery_id,
        'stripe_public_key': 'pk_test_51Lam8XGUiCQtdmRkzO1vpX4e89cf0Ogf1mBt2hHJ1UnDdKYNR65bPYd9QQiKCKyK2EoxhukvD3NUi52jrRxEPZSW00xl4EHDi0',
        'client_secret': 'test client secret key',
    }

    return render(request, template, context)
