# Generated by Django 4.1.3 on 2022-11-27 13:39

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_userprofile_default_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CamoPattern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('base_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('friendly_name', models.CharField(blank=True, max_length=50, null=True)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(blank=True, max_length=50, null=True)),
                ('base_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('friendly_name', models.CharField(blank=True, max_length=50, null=True)),
                ('base_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('image_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TechService',
            fields=[
                ('quote_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.TextField(blank=True, max_length=7000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='techquote', to='profiles.userprofile')),
                ('weapon_platform', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='wp', to='services.weaponplatform')),
                ('weapon_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ws', to='services.weaponsystem')),
            ],
        ),
        migrations.CreateModel(
            name='PaintService',
            fields=[
                ('quote_number', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('additional_info', models.TextField(blank=True, max_length=7000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('camo_pattern', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='camo', to='services.camopattern')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paintquote', to='profiles.userprofile')),
                ('weapon_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='weapon_sys', to='services.weaponsystem')),
            ],
        ),
    ]
