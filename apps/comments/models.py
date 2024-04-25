from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.general.services import normalize_text
from apps.users.models import CustomUser
from apps.products.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    message = models.CharField(max_length=300)
    rating = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_normalize_fields(self):
        return ['message']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
