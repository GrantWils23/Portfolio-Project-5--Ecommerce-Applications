from django.db import models


class DeliveryMethod(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False,)
    cost = models.DecimalField(max_digits=6, decimal_places=2,
                               null=False, default=3.50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name
