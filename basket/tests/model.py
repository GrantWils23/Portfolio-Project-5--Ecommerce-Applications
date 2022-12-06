from django.test import TestCase
from basket.models import DeliveryMethod


class DeliveryMethodModels(TestCase):

    def setUp(self):
        self.delivery = DeliveryMethod.objects.create(
            name='test_delivery',
            cost=3.50,
            friendly_name='test-del',
        )
        self.delivery.save()

    def tearDown(self):
        self.delivery.delete()

    def test_delivery_method_str(self):
        name = self.delivery
        self.assertEqual(str(name), "test_delivery")
