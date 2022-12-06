from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import DeliveryMethod
from .forms import DeliveryMethodForm
from checkout.forms import OrderForm


def view_basket(request):
    """ A view that returns basket page and its contents """

    if request.method == 'POST':
        orderform = OrderForm(request.POST)
        delivery = request.POST.get("delivery")
        if delivery == '1':
            d = DeliveryMethod.objects.get(id=1)
        elif delivery == '2':
            d = DeliveryMethod.objects.get(id=2)
        elif delivery == '3':
            d = DeliveryMethod.objects.get(id=3)
        request.session['deliveryfee'] = str(d.cost)
        request.session['delivery_id'] = str(d.pk)
        messages.success(request, f' {d.friendly_name}'
                         ' has been selected as shipping method')
    else:
        request.session['deliveryfee'] = str(3.50)
        request.session['delivery_id'] = str(1)
        orderform = OrderForm()
        orderform.save(commit=False)

    context = {
        'delivery_form': orderform,
    }
    return render(request, 'basket/basket.html', context)


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
        messages.success(
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
        # shopping basket reset back to standard shipping
        if len(basket) == 1:
            request.session['delivery'] = str(3.50)

        basket.pop(item_id)
        messages.warning(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@login_required
def add_delivery_method(request):
    """ Add a delivery to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DeliveryMethodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully Added new delivery method!')
            return redirect(reverse('add_delivery_method'))
        else:
            messages.error(
                request, 'Failed to add delivery method, \
                    Please ensure the form is valid.')
    else:
        form = DeliveryMethodForm()

    template = 'basket/add_delivery_method.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_delivery_method(request, delivery_method_id):
    """ Edit a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    deliverymethod = get_object_or_404(DeliveryMethod, pk=delivery_method_id)
    if request.method == 'POST':
        form = DeliveryMethodForm(
            request.POST, request.FILES, instance=deliverymethod)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Delivery!')
            return redirect(reverse('admin_controls'))
        else:
            messages.error(
                request, 'Failed to update delivery.\
                    Please ensure the form is valid.')
    else:
        form = DeliveryMethodForm(instance=deliverymethod)
        messages.info(
            request, f'You are editing {deliverymethod.friendly_name}')

    template = 'basket/edit_delivery_method.html'
    context = {
        'form': form,
        'deliverymethod': deliverymethod,
    }

    return render(request, template, context)


@login_required
def delete_delivery_method(request, delivery_method_id):
    """ Delete a delivery method from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    deliverymethod = get_object_or_404(DeliveryMethod, pk=delivery_method_id)
    deliverymethod.delete()
    messages.success(request, 'Delivery Method Deleted!')
    return redirect(reverse('admin_controls'))
