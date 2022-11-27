from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail

from .models import TechService, PaintService
from .models import WeaponPlatform, WeaponSystem, CamoPattern
from .forms import TechServiceForm, PaintServiceForm

from profiles.models import UserProfile


# Create your views here.

def send_tech_confirmation_email(quote):
    """ Send the user a confirmation email """
    cust_email = quote.email
    subject = render_to_string(
        'services/confirmation_emails/tech_confirmation_email_subject.txt',
        {'quote': quote})
    body = render_to_string(
        'services/confirmation_emails/tech_confirmation_email_body.txt',
        {'quote': quote, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


def send_paint_confirmation_email(quote):
    """ Send the user a confirmation email """
    cust_email = quote.email
    subject = render_to_string(
        'services/confirmation_emails/paint_confirmation_email_subject.txt',
        {'quote': quote})
    body = render_to_string(
        'services/confirmation_emails/paint_confirmation_email_body.txt',
        {'quote': quote, 'contact_email': settings.DEFAULT_FROM_EMAIL})
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )


def tech_services(request):
    """ Submit a Tech Service Enquiry """
    weapon_plat = WeaponPlatform.objects.all()
    weapon_sys = WeaponSystem.objects.all()
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the quote
        user_profile = profile
    else:
        profile = None
    print(profile)
    if request.method == 'POST':
        form_data = {
            'user_profile': profile,
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'weapon_platform': request.POST['weapon_platform'],
            'weapon_system': request.POST['weapon_system'],
            'adiitional_info': request.POST['additional_info'],
        }
        form = TechServiceForm(form_data, request.FILES)
        if form.is_valid():
            techservice = form.save(commit=False)
            TechService.calculate_estimate(techservice)
            techservice = form.save()
            messages.success(
                request, 'Succcess, your form has been submitted, an email shall be sent to you shortly')
            send_tech_confirmation_email(techservice)
            return redirect(reverse('thank_you'))
        else:
            messages.error(
                request, 'Failed to submit, Please ensure the form is valid.')
    else:
        form = TechServiceForm()

    template = 'services/tech_services.html'
    context = {
        'form': form,
        'weapon_plat': weapon_plat,
        'weapon_sys': weapon_sys,
    }

    return render(request, template, context)


def paint_services(request):
    """ Submit a Tech Service Enquiry """
    camo_pattern = CamoPattern.objects.all()
    weapon_sys = WeaponSystem.objects.all()
    profile = None
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the quote
        user_profile = profile
    else:
        profile = None
    print(profile)
    if request.method == 'POST':
        form_data = {
            'user_profile': profile,
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'camo_pattern': request.POST['camo_pattern'],
            'weapon_system': request.POST['weapon_system'],
            'adiitional_info': request.POST['additional_info'],
        }

        form = PaintServiceForm(form_data, request.FILES)
        if form.is_valid():
            paintservice = form.save(commit=False)
            PaintService.calculate_estimate(paintservice)
            paintservice = form.save()
            messages.success(
                request, 'Succcess, your form has been submitted, an email shall be sent to you shortly')
            send_paint_confirmation_email(paintservice)
            return redirect(reverse('thank_you'))
        else:
            messages.error(
                request, 'Failed to submit, Please ensure the form is valid.')
    else:
        form = PaintServiceForm()

    template = 'services/paint_services.html'
    context = {
        'form': form,
        'camo_pattern': camo_pattern,
        'weapon_sys': weapon_sys,
    }

    return render(request, template, context)


def thank_you(request):
    """ from completion page """

    template = 'services/thank_you.html'

    return render(request, template,)
