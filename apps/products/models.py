from django.db import models
from apps.categories.models import MainCategory, SubCategory
from django.core.exceptions import ValidationError
from django.utils.translation import get_language
from apps.features.models import FeatureValue
from apps.general.services import normalize_text


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
    
    def get_features(self):
        features = {}
        feature_values = FeatureValue.objects.filter(product_features__product_id=self.pk).distinct().select_related('feature')
        for feature_value in feature_values:
            feature_id = feature_value.feature_id
            value = {'id':feature_value.pk, 'name':feature_value.get_value}
            if feature_id not in features:
                features[feature_id] = {'name':feature_value.feature.get_name, 'values':[value]}
            else:
                features[feature_id]['values'].append(value)
        return features 
    
    def save(self, *args, **kwargs):
        if self.sub_category:
            self.main_category = self.sub_category.main_category
        normalize_text(self)
        super().save(*args, **kwargs)
    
    def get_category(self):
        return self.main_category or self.sub_category

    def clean(self):
        if (bool(self.main_category) + bool(self.sub_category)) != 1:
            raise ValidationError('bittasini tanla')
        
    def feature(self):
        return self.product_features.order_by('price').first()
        
    def first_image(self):
        return self.image_product.first()

    def __str__(self):
        return self.title_uz


class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='image_product')
    ordering_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.product.title_uz} image'

    class Meta:
        unique_together = ('product', 'ordering_number')
