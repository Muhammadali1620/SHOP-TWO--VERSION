from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from apps.general.services import normalize_text
from apps.products.models import Product
from apps.categories.models import MainCategory, SubCategory
from django.utils.translation import get_language


class Feature(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT,
                                        blank=True, null=True)
    ordering_number = models.PositiveSmallIntegerField(unique=True)
    name_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ' Feature'

    def get_category(self):
        return self.main_category or self.sub_category
    
    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('Bitta Category ni tanla')
        
    def get_name(self):
        return getattr(self, f'name_{get_language()}')
    
    def get_normalize_fields(self):
        return ['name_uz', 'name_ru']

    def save(self, *args, **kwargs):
        if self.sub_category:
            self.main_category = self.sub_category.main_category
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name_uz


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='values')
    value_uz = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)
    value_ru = models.CharField(max_length=30, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_value(self):
        return getattr(self, f'value_{get_language()}')
    
    def get_normalize_fields(self):
        return ['value_uz', 'value_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.feature}:{self.value_uz}'

    class Meta:
        unique_together = ('feature', 'slug')
     


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_features')
    feature_value = models.ManyToManyField(FeatureValue, related_name='product_features', blank=True)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)], help_text="Narxni so'mda kiriting")
    
    created_at = models.DateTimeField(auto_now_add=True)