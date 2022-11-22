from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, EditUserProfileForm

from checkout.models import Order


def profile(request):
    """ Display the User's profile """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
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
