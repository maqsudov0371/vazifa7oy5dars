from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=13, blank=True, null=True, db_index=True)
    auth_code = models.CharField(max_length=6, blank=True)

    def __str__(self) -> str:
        return f"{self.username}"
    

class Musican(models.Model):
    
    

class Podca(models.Model):
    title = models.CharField(max_length=100)
    musican = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    music = models.FileField(upload_to='media/music')
    image = models.ImageField(upload_to='media/images')
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    