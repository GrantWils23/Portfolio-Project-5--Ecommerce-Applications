from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .filters import OrdersFilter, PaintQuoteFilter, TechQuoteFilter

from checkout.models import Order
from services.models import PaintService, TechService


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


@login_required
def admin_controls(request):
    """ A view that returns the admin controls panel """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to that view.')
        return redirect(reverse('home'))
    return render(request, 'home/admin_controls.html')


@login_required
def admin_view_orders(request):
    """ return a list of all orders to the admin """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to that view.')
        return redirect(reverse('home'))
    orders = Order.objects.all().order_by("-date")
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


# ///////////////////////////////////////////////////////////////////////////////


@login_required
def admin_view_paint_quotes(request):
    """ return a list of all paint quotes to the admin """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to that view.')
        return redirect(reverse('home'))
    quotes = PaintService.objects.all().order_by("-date")
    quotes_filter = PaintQuoteFilter(request.GET, queryset=quotes)
    template = 'home/paint_job_quotes.html'
    context = {
        'quotes_filter': quotes_filter,
    }
    return render(request, template, context)


@login_required
def admin_view_paintjob(request, quote_number):
    """ return a specific paint quote for the admin to view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    quote = get_object_or_404(PaintService, quote_number=quote_number)

    template = 'home/paint_job_detail.html'
    context = {
        'quote': quote,
    }
    return render(request, template, context)


@login_required
def delete_paint_quote(request, quote_number):
    """ Delete a paint quote from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    quote = get_object_or_404(Order, quote_number=quote_number)
    quote.delete()
    messages.success(request, 'Quote Deleted!')
    return redirect(reverse('admin_view_orders'))


# //////////////////////////////////////////////////////////////////////////

@login_required
def admin_view_tech_quotes(request):
    """ return a list of all tech quotes to the admin """
    if not request.user.is_superuser:
        messages.error(request,
                       'Sorry, only store owners have access to that view.')
        return redirect(reverse('home'))
    quotes = TechService.objects.all().order_by("-date")
    quotes_filter = TechQuoteFilter(request.GET, queryset=quotes)
    template = 'home/tech_job_quotes.html'
    context = {
        'quotes_filter': quotes_filter,
    }
    return render(request, template, context)


@login_required
def admin_view_techjob(request, quote_number):
    """ return a specific tech quote for the admin to view """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    quote = get_object_or_404(TechService, quote_number=quote_number)

    template = 'home/tech_job_detail.html'
    context = {
        'quote': quote,
    }
    return render(request, template, context)


@login_required
def delete_tech_quote(request, quote_number):
    """ Delete a tech quote from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    quote = get_object_or_404(Order, quote_number=quote_number)
    quote.delete()
    messages.success(request, 'Quote Deleted!')
    return redirect(reverse('admin_view_orders'))
