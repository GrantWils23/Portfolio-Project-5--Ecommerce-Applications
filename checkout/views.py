from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from basket.models import DeliveryMethod


from .forms import OrderForm
from .models import Order


def checkout(request):
    """ The view that returns the checkout page """
    delivery_id = request.session.get('delivery_id')    # delivery_id availble from the context basket... insert into the order from delivery field
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
    }

    return render(request, template, context)
