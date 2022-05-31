from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Register(models.Model):
    first_name: str = models.CharField(max_length=200)
    last_name: str = models.CharField(max_length=200)
    email: str = models.EmailField(max_length=254)
    address: str = models.CharField(max_length=200)
    type_of_housing: str = models.CharField(max_length=200)
    country: str = models.CharField(max_length=200)
    department: str = models.CharField(max_length=200)
    city: str = models.CharField(max_length=200)
    comments: str = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name
