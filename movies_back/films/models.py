from django.db import models
from django.utils import timezone

class Language(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    name = models.CharField(max_length=200, default=None, null=True)
    description = models.CharField(max_length=400, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    
class Category(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    name = models.CharField(max_length=200, default=None, null=False)
    last_update = models.DateTimeField(default=timezone.now, null=False)

class Actor(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    first_name = models.CharField(max_length=200, default=None, null=False)
    last_name = models.CharField(max_length=200, default=None, null=False)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    
class Films(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    title = models.CharField(max_length=200, default=None, null=True)
    description = models.CharField(max_length=400, default=None, null=True)
    release_year = models.CharField(max_length=200, default=None, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, default=None, null=True)
    rental_duration = models.IntegerField(default=0, null=False)
    rental_rate = models.IntegerField(default=0, null=False)
    replacment_cost = models.FloatField(default=0.0)
    rating = models.IntegerField(default=0, null=True, blank=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
    special_features = models.CharField(max_length=200, default=None, null=True)
    fulltext = models.CharField(max_length=400, default=None, null=True)

class FilmActor(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)

    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, default=None, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)

class FilmCategory(models.Model):
    id = models.AutoField(
        primary_key=True, editable=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, null=True)
    film = models.ForeignKey(Films, on_delete=models.CASCADE, default=None, null=True)
    last_update = models.DateTimeField(default=timezone.now, null=False)
