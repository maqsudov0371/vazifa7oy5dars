# admin.py
from django.contrib import admin
from .models import User, Musican, Podca

class UserAdmin(admin.ModelAdmin):
    pass

class MusicanAdmin(admin.ModelAdmin):
    pass

class PodcaAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Musican, MusicanAdmin)
admin.site.register(Podca, PodcaAdmin)
