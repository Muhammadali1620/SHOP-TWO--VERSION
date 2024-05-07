# Generated by Django 5.0.4 on 2024-05-07 12:34

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering_number', models.PositiveSmallIntegerField(unique=True)),
                ('name_uz', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('name_ru', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.maincategory')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory')),
            ],
            options={
                'verbose_name_plural': ' Feature',
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_uz', models.CharField(max_length=30)),
                ('slug', models.SlugField(max_length=30)),
                ('value_ru', models.CharField(blank=True, max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='features.feature')),
            ],
            options={
                'unique_together': {('feature', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, help_text="Narxni so'mda kiriting", max_digits=20, validators=[django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('feature_value', models.ManyToManyField(blank=True, related_name='product_features', to='features.featurevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_features', to='products.product')),
            ],
        ),
    ]
