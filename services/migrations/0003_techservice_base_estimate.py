# Generated by Django 4.1.3 on 2022-11-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_paintservice_base_estimate'),
    ]

    operations = [
        migrations.AddField(
            model_name='techservice',
            name='base_estimate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
