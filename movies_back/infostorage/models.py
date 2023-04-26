from django.db import models
from django.utils import timezone

class Country(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    country = models.CharField(max_length=200, default=None, null=False)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    
class City(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    city = models.CharField(max_length=200, default=None, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    
class Address(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)
    address = models.CharField(max_length=200, default=None, null=False)
    district = models.CharField(max_length=200, default=None, null=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=None, null=True)
    postal_code = models.CharField(max_length=200, default=None, null=False)
    phone = models.CharField(max_length=200, default=None, null=False)
    last_update = models.DateTimeField(default=timezone.now, null=False)
