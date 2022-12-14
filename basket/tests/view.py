from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product, Category, Brand

from basket.models import DeliveryMethod


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

    def test_view_basket_GET(self):
        response = self.client.get(reverse('view_basket'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
