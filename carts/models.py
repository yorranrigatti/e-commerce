import uuid

from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone


class Product(models.Model):
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    subtotal