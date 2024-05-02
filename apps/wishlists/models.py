from django.db import models
from apps.users.models import CustomUser
from apps.products.models import Product

 
class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='wishlist')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)
