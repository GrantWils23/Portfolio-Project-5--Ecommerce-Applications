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
    path('admin_controls/view_orders/', views.admin_view_orders,
         name='admin_view_orders'),
    path('admin_controls/view_order/<int:order_id>',
         views.admin_view_specific_order,
         name='admin_view_specific_order'),
    path('admin_controls/view_orders/delete/<int:order_id>',
         views.delete_order, name='delete_order'),
    path('admin_controls/view_paint_quotes/', views.admin_view_paint_quotes,
         name='admin_view_paint_quotes'),
    path('admin_controls/view_paintjob/<int:quote_number>',
         views.admin_view_paintjob,
         name='admin_view_paintjob_details'),
    path('admin_controls/view_orders/paint/delete/<int:quote_number>',
         views.delete_order, name='delete_paint_quote'),
    path('admin_controls/view_tech_quotes/', views.admin_view_tech_quotes,
         name='admin_view_tech_quotes'),
    path('admin_controls/view_techjob/<int:quote_number>',
         views.admin_view_techjob,
         name='admin_view_techjob_details'),
    path('admin_controls/view_orders/tech/delete/<int:quote_number>',
         views.delete_order, name='delete_tech_quote'),
]
