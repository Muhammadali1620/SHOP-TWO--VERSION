from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.general.services import normalize_text
from apps.users.models import CustomUser
from apps.products.models import Product


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=300, blank=True)
    message = models.CharField(max_length=300)
    rating = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_normalize_fields(self):
        return ['message']

    def save(self, *args, **kwargs):
        normalize_text(self)
        if self.user:
            self.name, self.email = self.user.first_name, self.user.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
