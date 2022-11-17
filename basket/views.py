from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from .models import DeliveryMethod
from checkout.forms import DeliveryForm




def view_basket(request):
    """ A view that returns basket page and its contents """
    if request.method == 'POST':
        deliveryform = DeliveryForm(request.POST)
        delivery = request.POST.get("delivery")
        if delivery == '1':
            delivery_method = DeliveryMethod.objects.get(id=1)
        elif delivery == '2':
            delivery_method = DeliveryMethod.objects.get(id=2)
        elif delivery == '3':
            delivery_method = DeliveryMethod.objects.get(id=3)
        request.session['delivery'] = str(delivery_method.delivery_method_cost)
    else:
        deliveryform = DeliveryForm()

    context = {
        'deliveryform': deliveryform,
    }
    return render(request, 'basket/basket.html', context)


def update_delivery_method(request, delivery_id):
    """ A view that returns a form for a delivery method for the order """

    deliverymethod = get_object_or_404(DeliveryMethod, pk=delivery_id)
    delivery = request.session.get('delivery')

    delivery = DeliveryMethod.delivery_method_cost


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'Updated {product.name}'
            f' quantity to {basket[item_id]}'
        )
    else:
        basket[item_id] = quantity
        messages.success(request, f' x {basket[item_id]}'
                         f' {product.name} has been added to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Adjust the qty of the specified product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.info(
            request, f'Updated {product.name}'
            f' quantity to {basket[item_id]}'
        )
    else:
        basket.pop(item_id)
        messages.info(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def remove_from_basket(request, item_id):
    """ Remove the item from the shopping basket """

    try:
        product = get_object_or_404(Product, pk=item_id)
        basket = request.session.get('basket', {})

        basket.pop(item_id)
        messages.warning(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
