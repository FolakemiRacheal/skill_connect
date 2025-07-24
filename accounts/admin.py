from django.contrib import admin

# Register your models here.
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_freelancer', 'is_client', 'is_staff')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_freelancer', 'is_client')}),
    )

admin.site.register(User, UserAdmin)
