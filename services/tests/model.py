from django.test import TestCase
from services.models import (
    WeaponPlatform,
    WeaponSystem,
    CamoPattern,
    TechService,
    PaintService,
)


class TestServiceModels(TestCase):

    def setUp(self):

        self.testplatform = WeaponPlatform.objects.create(
            name="testPlat",
            friendly_name="test",
            base_price=10)
        self.testplatform.save()

        self.testsystem = WeaponSystem.objects.create(
            name="testSys",
            friendly_name="test",
            base_price=20)
        self.testsystem.save()

        self.testcamo = CamoPattern.objects.create(
            name="testCamo",
            friendly_name="test",
            base_price=15)
        self.testcamo.save()

    def tearDown(self):
        self.testplatform.delete()
        self.testcamo.delete()
        self.testsystem.delete()

    def test_weapon_platform_model_str(self):
        name = WeaponPlatform.objects.create(name="Django Testing")
        friendly_name = WeaponPlatform.objects.create(
            friendly_name="Django test"
            )
        self.assertEqual(str(name), "Django Testing")
        self.assertEqual(friendly_name.get_friendly_name(), "Django test")

    def test_weapon_system_model_str(self):
        name = WeaponSystem.objects.create(name="Django Testing")
        friendly_name = WeaponSystem.objects.create(
            friendly_name="Django test"
            )
        self.assertEqual(str(name), "Django Testing")
        self.assertEqual(friendly_name.get_friendly_name(), "Django test")

    def test_camo_pattern_model_str(self):
        name = CamoPattern.objects.create(name="Django Testing")
        friendly_name = CamoPattern.objects.create(
            friendly_name="Django test"
            )
        self.assertEqual(str(name), "Django Testing")
        self.assertEqual(friendly_name.get_friendly_name(), "Django test")

    def test_paint_service_model_str(self):
        order = PaintService.objects.create(
            quote_number=1, full_name="TestName",
            email="Test@test.com",
            camo_pattern=self.testcamo,
            weapon_system=self.testsystem,
            )
        order.calculate_estimate()
        order.save()

        self.assertEqual(str(order), "Paint service")
        self.assertEqual(order.base_estimate, 35)

    def test_tech_service_model_str(self):
        order2 = TechService.objects.create(
            quote_number=2, full_name="TestName",
            email="Test@test.com",
            weapon_platform=self.testplatform,
            weapon_system=self.testsystem,
            )
        order2.calculate_estimate()
        order2.save()

        self.assertEqual(str(order2), "Tech service")
        self.assertEqual(order2.base_estimate, 30)
