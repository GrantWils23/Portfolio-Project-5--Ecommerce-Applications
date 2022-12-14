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
    path('', views.view_basket, name="view_basket"),
    path('add/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('adjust/<item_id>/', views.adjust_basket, name='adjust_basket'),
    path('remove/<item_id>/', views.remove_from_basket,
         name='remove_from_basket'),
    path('add_delivery_method/', views.add_delivery_method,
         name='add_delivery_method'),
    path('edit_delivery_method/<int:delivery_method_id>/',
         views.edit_delivery_method, name='edit_delivery_method'),
    path('delete_delivery_method/<int:delivery_method_id>/',
         views.delete_delivery_method, name='delete_delivery_method'),
]
