from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.general.validators import phone_validate
from apps.users.managers import CustomUserManager

  
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    first_name = models.CharField(max_length=70, blank=True)
    last_name = models.CharField(max_length=70, blank=True)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], blank=True)
    address1 = models.CharField(max_length=300, blank=True)
    address2 = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    zip_code = models.PositiveSmallIntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-pk']


class UserAuthCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)

    expire_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.email