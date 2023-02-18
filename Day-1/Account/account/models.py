from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ADMIN = 'ADMIN'
    CUSTOMER = 'CUSTOMER'
    ROLE = [(ADMIN, 'Admin'), (CUSTOMER, 'Customer')]
    
    profile_photo = models.ImageField(verbose_name="Photo de profil")
    role = models.CharField(max_length = 50, choices=ROLE, verbose_name='Role')