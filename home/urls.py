"""airsoft_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services, name='services'),
    path('faqs/', views.faqs, name='faqs'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('sitemap/', views.sitemap_page, name='sitemap'),
    path('about_us/', views.about_us, name='about_us'),
    path('admin_controls/', views.admin_controls, name='admin_controls'),
]
