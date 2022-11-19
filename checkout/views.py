from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from basket.models import DeliveryMethod
from django.conf import settings


from .forms import OrderForm
from .models import Order
from basket.contexts import basket_contents

import stripe


def checkout(request):
    """ The view that returns the checkout page """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

# -------------------------------------------------------------------------
    delivery_id = request.session.get('delivery_id')  # del_id from context.py
    delivery_method = get_object_or_404(DeliveryMethod, pk=delivery_id)

    initial_data = {
        'delivery': delivery_id,
    }
# -------------------------------------------------------------------------

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('products'))

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    order_form = OrderForm(initial=initial_data)  # initial data
    template = 'checkout/checkout.html'
    context = {
        'delivery_method': delivery_method,
        'order_form': order_form,
        'delivery_id': delivery_id,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
