from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import resolve

from .models import UserProfile
from .forms import UserProfileForm, EditUserProfileForm

from checkout.models import Order
from products.models import Product


@login_required
def profile(request):
    """ Display the User's profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    products = Product.objects.filter(users_wishlist=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'products': products,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def EditUserProfile(request):
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully')
            return redirect(reverse('profile'))
    else:
        form = EditUserProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'profiles/edit_profile.html', args)


@login_required
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.info(request, 'Password updated successfully')
            return redirect(reverse('profile'))
        else:
            return redirect('change_password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'profiles/change_password.html', args)


#  ##### --------------- wishlist ---------------- ######


@login_required
def add_to_wishlist(request, product_id):
    pk = request.GET.get('product_id')
    product = get_object_or_404(Product, pk=product_id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user.id)
        messages.warning(request, f'{product.name} Removed from your wishlist')
    else:
        product.users_wishlist.add(request.user.id)
        messages.success(request, f'{product.name} added to your wishlist')
    return redirect(reverse('product_detail', args=[product.id]))
