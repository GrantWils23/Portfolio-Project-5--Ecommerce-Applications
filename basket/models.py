from django.db import models


class DeliveryMethod(models.Model):
    delivery_method_name = models.CharField(max_length=50, null=False, blank=False,)
    delivery_method_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=3.50)


    def __str__(self):
        return self.delivery_method_name
