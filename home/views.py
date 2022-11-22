from django.shortcuts import render

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
