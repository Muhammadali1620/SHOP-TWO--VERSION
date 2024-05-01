from django.db import models
from django.core.exceptions import ValidationError
from apps.general.services import normalize_text
from apps.users.models import CustomUser

 
class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (self.name and self.email) and not self.user:
           raise ValidationError('name and email are required')
        
    def save(self, *args, **kwargs):
        if self.user:
            self.name, self.email = self.user.name, self.user.email
        super().save(*args, **kwargs)
    
    def get_normalize_fields(self):
        return ['title', 'message', 'name']

    def save(self, *args, **kwargs):
        normalize_text(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}:{self.title}'