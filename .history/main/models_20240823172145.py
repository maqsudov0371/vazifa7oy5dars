from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True, db_index=True)
    auth_code = models.CharField(max_length=6, blank=True)

    def __str__(self) -> str:
        return f"{self.username}"
    

class