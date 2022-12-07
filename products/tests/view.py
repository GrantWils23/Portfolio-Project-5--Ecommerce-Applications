from django.test import TestCase, Client
from django.urls import reverse

from products.models import Product, Category, Brand


class TestProductViews(TestCase):

    def setUp(self):
        self.client = Client()

        self.brand = Brand.objects.create(
            name='brand',
            friendly_name='brand',
        )
        self.category = Category.objects.create(
            name='cat',
            friendly_name='cat',
        )
        self.product = Product.objects.create(
            id=1,
            name='item',
            category=self.category,
            brand=self.brand,
            sku='101',
            description='test stuff',
            price=10.00,
            rating=5,
        )

    def test_view_all_products_GET(self):
        response = self.client.get(reverse('products'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_view_product_detail_GET(self):
        response = self.client.get(
            reverse('product_detail', args=[self.product.pk]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
