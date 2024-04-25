from django.db import models
from apps.features.models import ProductFeature
from apps.users.models import CustomUser



class Cart(models.Model): 
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ProductFeature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE)
    counts = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email