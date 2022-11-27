import uuid
from django.db import models
from django.db.models import Sum
from phonenumber_field.modelfields import PhoneNumberField

from profiles.models import UserProfile


class WeaponSystem(models.Model):
    """ pistol, smg, etc... """
    name = models.CharField(max_length=50, null=False, blank=False)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class WeaponPlatform(models.Model):
    """ gas, electric, gas """
    name = models.CharField(max_length=50, null=False, blank=False)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CamoPattern(models.Model):
    """ range of camo patterns """
    name = models.CharField(max_length=50, null=False, blank=False)
    base_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class PaintService(models.Model):
    quote_number = models.BigAutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='paintquote')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    camo_pattern = models.ForeignKey('CamoPattern', null=True, blank=False,
                                     on_delete=models.SET_NULL, related_name='camo')
    weapon_system = models.ForeignKey('WeaponSystem', null=True, blank=False,
                                      on_delete=models.SET_NULL, related_name='weapon_sys')
    additional_info = models.TextField(max_length=7000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    base_estimate = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f"paint service"

    def calculate_estimate(self):
        """ return estimate price for admin """
        self.base_estimate = self.camo_pattern.base_price + self.weapon_system.base_price
        self.save()


class TechService(models.Model):
    quote_number = models.BigAutoField(primary_key=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='techquote')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    weapon_platform = models.ForeignKey('WeaponPlatform', null=True, blank=False,
                                        on_delete=models.SET_NULL, related_name='wp')
    weapon_system = models.ForeignKey('WeaponSystem', null=True, blank=False,
                                      on_delete=models.SET_NULL, related_name='ws')
    additional_info = models.TextField(max_length=7000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    base_estimate = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def __str__(self):
        return f"paint service"

    def calculate_estimate(self):
        """ return estimate price for admin """
        self.base_estimate = self.weapon_platform.base_price + self.weapon_system.base_price
        self.save()
