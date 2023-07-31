from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from.models import Record

class CustomUserAdmin(BaseUserAdmin):
    # Remove the 'change password' fieldset from the fieldsets list
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    
admin.site.register(Record)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)