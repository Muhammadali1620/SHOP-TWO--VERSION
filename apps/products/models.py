from django.db import models
from django.core.validators import MinValueValidator
from apps.categories.models import MainCategory, SubCategory
from django.core.exceptions import ValidationError
from django.utils.translation import get_language
from apps.general.services import normalize_text
from apps.products.services import get_usd_price
from math import ceil


class Product(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    title_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title_ru = models.CharField(max_length=100, blank=True)
    short_desc_uz = models.CharField(max_length=250)
    short_desc_ru = models.CharField(max_length=250, blank=True)
    long_desc_uz = models.TextField(max_length=1500)
    long_desc_ru = models.TextField(max_length=1500, blank=True)
    review_counts = models.PositiveSmallIntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_title(self):
        return getattr(self, f'title_{get_language()}')
    
    def get_short(self):
        return getattr(self, f'short_desc_{get_language()}')
    
    def get_long(self):
        return getattr(self, f'long_desc_{get_language()}')
    
    def get_normalize_fields(self):
        return ['title_uz', 'title_ru', 'short_desc_uz', 'short_desc_ru', 'long_desc_uz', 'long_desc_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)
    
    def get_category(self):
        return self.main_category or self.sub_category

    def get_price_in_usd(self):
        in_usd = get_usd_price()
        price = float(self.price) / in_usd
        return ceil(price)

    def get_old_price_in_usd(self):
        in_usd = get_usd_price()
        price = float(self.old_price) / in_usd
        return ceil(price)

    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('bittasini tanla')

    def __str__(self):
        return self.title_uz


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordering_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.product.title_uz} image'

    class Meta:
        unique_together = ('product', 'ordering_number')
