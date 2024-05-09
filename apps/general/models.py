from django.db import models
from django.core.exceptions import ValidationError
from apps.general.validators import phone_validate
from apps.categories.models import SubCategory
from django.utils.translation import get_language
from apps.general.services import next_10_days, normalize_text
from django.utils.timezone import now


class SocialLink(models.Model):
    icon = models.ImageField(upload_to='general/social_link/icon/', blank=True, null=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    link = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_normalize_fields(self):
        return ['name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=35, unique=True)
    logo = models.ImageField(upload_to="general/payment_method/logo/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_normalize_fields(self):
        return ['name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class General(models.Model):
    stor_name = models.CharField(max_length=20)
    shipping = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    logo = models.ImageField(upload_to='general/logotype/image/')
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    email = models.EmailField()
    address_uz = models.CharField(max_length=100)
    address_ru = models.CharField(max_length=100, blank=True)
    desc_uz = models.TextField(max_length=1000)
    desc_ru = models.TextField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_address(self):
        return getattr(self, f'address_{get_language()}')
    
    def get_desc(self):
        return getattr(self, f'desc_{get_language()}')
    
    def get_normalize_fields(self):
        return ['address_uz', 'address_ru', 'desc_uz', 'desc_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)


    
    def __str__(self):
        return self.stor_name


class Service(models.Model):
    title_uz = models.CharField(max_length=100)
    title_ru = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='general/service/icon/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_title(self):
        return getattr(self, f'title_{get_language()}')
    
    def get_normalize_fields(self):
        return ['title_uz', 'title_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Branch(models.Model):
    image = models.FileField(upload_to='general/image', blank=True, null=True)
    title_uz = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    title_ru = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_title(self):
        return getattr(self, f'title_{get_language()}')
    
    def get_normalize_fields(self):
        return ['title_uz', 'title_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Banner(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title_ru = models.CharField(max_length=100, blank=True)
    desc_uz = models.CharField(max_length=500)
    desc_ru = models.CharField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_title(self):
        return getattr(self, f'title_{get_language()}')

    def get_desc(self):
        return getattr(self, f'desc_{get_language()}')
    
    def get_normalize_fields(self):
        return ['title_uz', 'title_ru', 'desc_uz', 'desc_ru']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title_uz


class Coupon(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=12, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="So'mda yoki foizda kiriting!!!")
    amount_is_percent = models.BooleanField(default=True)
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=next_10_days())

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_normalize_fields(self):
        return ['title']

    def save(self, *args, **kwargs):
        normalize_text(self)
        self.code = ''.join(self.code.split())
        super().save(*args, **kwargs)

    def clean(self):
        if self.amount_is_percent and not (1 <= self.amount < 100):
            raise ValidationError({'amount':'Invalid ammount [1- 99]'})

    def __str__(self):
        return self.title
