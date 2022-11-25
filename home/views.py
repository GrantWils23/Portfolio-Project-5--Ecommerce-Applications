from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .filters import OrdersFilter

from checkout.models import Order

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def services(request):
    """ A view that displays the services page """
    return render(request, 'home/services_page.html')


def faqs(request):
    """ A view that displays the FAQs page """
    return render(request, 'home/faqs.html')


def contact_us(request):
    """ A view that displays the contact us page"""
    return render(request, 'home/contact_us.html')


def privacy_policy(request):
    """ A view that displays the privacy policy """
    return render(request, 'home/privacy_policy.html')


def sitemap_page(request):
    """ A view that displays the sitemap """
    return render(request, 'home/sitemap.html')


def about_us(request):
    """ A view that displays the about us page"""
    return render(request, 'home/about_us.html')


def admin_controls(request):
    """ A view that returns the admin controls panel """
    return render(request, 'home/admin_controls.html')


@login_required
def admin_view_orders(request):
    """ return a list of all bookings to the admin """
    orders = Order.objects.all()
    orders_filter = OrdersFilter(request.GET, queryset=orders)
    template = 'home/admin_orders_list.html'
    context = {
        'orders_filter': orders_filter,
    }
    return render(request, template, context)


@login_required
def admin_view_specific_order(request, order_id):
    """ return a specific order for the admin to view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, id=order_id)

    template = 'home/admin_order_preview.html'
    context = {
        'order': order,
    }
    return render(request, template, context)


@login_required
def delete_order(request, order_id):
    """ Delete a category from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    messages.success(request, 'Order Deleted!')
    return redirect(reverse('admin_view_orders'))

