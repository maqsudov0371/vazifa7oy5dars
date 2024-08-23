# admin.py
from django.contrib import admin
from .models import User, Musican, Podca

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Musican)
class MusicanAdmin(admin.ModelAdmin):
    pass

@admin.register(Podca)
class PodcaAdmin(admin.ModelAdmin):
    pass
