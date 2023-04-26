from django.db import models
from django.db.models import Sum
from django.utils import timezone
from infostorage.models import *
from films.models import *


class Staff(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    first_name = models.CharField(max_length=200, default=None, null=False)
    last_name = models.CharField(max_length=200, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    email = models.CharField(max_length=200, default=None, null=False)
    active = models.BooleanField(default=False)
    username = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=200, null=False)
    last_update = models.DateTimeField(default=timezone.now, null=True)
    picture =  models.CharField(max_length=200, null=False)
    
class Store(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    manager_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, null=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    
class Rental(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, default=None, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
        
class Inventory(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)

class Customer(models.Model):
    """Customer Model"""
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(max_length=200, default=None, null=False)
    last_name = models.CharField(max_length=200, default=None, null=False)
    email = models.CharField(max_length=200, default=None, null=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, default=None, null=True)
    active = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=True)
    
class Payment(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, null=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, default=None, null=True)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, default=None, null=True)
    amount = models.FloatField(default=0.0)
    payment_date = models.DateTimeField(default=timezone.now, null=False)
