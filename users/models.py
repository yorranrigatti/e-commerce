import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from users.utils import CustomUser


class User(AbstractUser):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email           = models.EmailField(max_length=255, unique=True)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)
    birth_date      = models. DateField()
    created_at      = models.DateTimeField(default=timezone.now)
    updated_at      = models.DateTimeField(auto_now=True)
    username        = None
    REQUIRED_FIELDS = ["first_name", "last_name", "birth_date"]
    USERNAME_FIELD  = "email"

    cart            = models.ForeignKey('carts.Cart', related_name='user', blank=True, null=True, on_delete=models.CASCADE)
    
    objects         = CustomUser()
