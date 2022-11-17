# Generated by Django 4.1.3 on 2022-11-16 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_method_name', models.CharField(max_length=50)),
                ('delivery_method_cost', models.DecimalField(decimal_places=2, default=3.5, max_digits=6)),
            ],
        ),
    ]
