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
    path('tech_services/', views.tech_services, name='tech_services'),
    path('paint_services/', views.paint_services, name='paint_services'),
    path('thank_you/', views.thank_you, name='thank_you'),
    ]
#     path('<int:product_id>/', views.product_detail, name='product_detail'),
#     path('add_product/', views.add_product, name='add_product'),
#     path('add_brand/', views.add_brand, name='add_brand'),
#     path('add_category/', views.add_category, name='add_category'),
#     path('edit_product/<int:product_id>/',
#          views.edit_product, name='edit_product'),
#     path('edit_brand/<int:brand_id>/',
#          views.edit_brand, name='edit_brand'),
#     path('edit_category/<int:category_id>/',
#          views.edit_category, name='edit_category'),
#     path('delete_product/<int:product_id>/',
#          views.delete_product, name='delete_product'),
#     path('delete_brand/<int:brand_id>/',
#          views.delete_brand, name='delete_brand'),
#     path('delete_category/<int:category_id>/',
#          views.delete_category, name='delete_category'),
