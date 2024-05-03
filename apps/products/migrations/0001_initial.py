# Generated by Django 5.0.4 on 2024-05-03 05:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_uz', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('title_ru', models.CharField(blank=True, max_length=100)),
                ('short_desc_uz', models.CharField(max_length=250)),
                ('short_desc_ru', models.CharField(blank=True, max_length=250)),
                ('long_desc_uz', models.TextField(max_length=1500)),
                ('long_desc_ru', models.TextField(blank=True, max_length=1500)),
                ('review_counts', models.PositiveSmallIntegerField(default=0)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.maincategory')),
                ('sub_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categories.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products/%Y/%m/%d/')),
                ('ordering_number', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_product', to='products.product')),
            ],
            options={
                'unique_together': {('product', 'ordering_number')},
            },
        ),
    ]
