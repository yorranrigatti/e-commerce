import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Product(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    brand       = models.CharField(max_length=255)
    model       = models.CharField(max_length=255)
    variation   = models.CharField(max_length=255, null=True)
    price       = models.FloatField()
    description = models.CharField(max_length=1000)
    colors      = ArrayField(models.CharField(max_length=64), null=True)
    sizes       = ArrayField(models.CharField(max_length=5))
    category    = models.CharField(max_length=255, null=True)
    inventory   = models.IntegerField(default=0)
    created_at  = models.DateTimeField(default=timezone.now)
    updated_at  = models.DateTimeField(auto_now=True)
