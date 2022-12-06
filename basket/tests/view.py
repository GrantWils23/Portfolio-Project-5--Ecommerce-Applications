from django.test import TestCase, Client
from django.urls import resolve, reverse
from products.models import Product, Category, Brand, UserProfile

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from basket.models import DeliveryMethod
from basket.forms import DeliveryMethodForm
from checkout.forms import OrderForm
from basket.views import (
    view_basket,
    add_to_basket,
    adjust_basket,
    remove_from_basket,
    add_delivery_method,
    edit_delivery_method,
    delete_delivery_method,
    )


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.delmeth = DeliveryMethod.objects.create(
            name="test-delmeth", cost=1.5, friendly_name="test-del"
            )
        self.brand = Brand.objects.create(
            name='brand',
            friendly_name='brand',
        )
        self.category = Category.objects.create(
            name='cat',
            friendly_name='cat',
        )
        self.product = Product.objects.create(
            name='item',
            category=self.category,
            brand=self.brand,
            sku='101',
            description='test stuff',
            price=10.00,
            rating=5,
        )

        self.delivform = DeliveryMethodForm(self.delmeth)

    def test_view_basket_GET(self):
        response = self.client.get(reverse('view_basket'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
