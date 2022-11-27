from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import TechService, PaintService
from .models import WeaponPlatform, WeaponSystem, CamoPattern
from .forms import TechServiceForm, PaintServiceForm

from profiles.models import UserProfile


# Create your views here.


def tech_services(request):
    """ Submit a Tech Service Enquiry """
    weapon_plat = WeaponPlatform.objects.all()
    weapon_sys = WeaponSystem.objects.all()    

    if request.method == 'POST':
        form = TechServiceForm(request.POST, request.FILES)
        if form.is_valid():
            techservice = form.save()
            messages.success(
                request, 'Succcess, your form has been submitted, an email shall be sent to you shortly')
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

    if request.method == 'POST':
        form = PaintServiceForm(request.POST, request.FILES)
        if form.is_valid():
            paintservice = form.save()
            messages.success(
                request, 'Succcess, your form has been submitted, an email shall be sent to you shortly')
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
