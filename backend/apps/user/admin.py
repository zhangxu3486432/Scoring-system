from django.contrib import admin

from .models import UserModel


class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'code']
    list_display = ['username', 'email', 'code', 'is_activate', 'is_staff', 'is_superuser']
    readonly_fields = ['code']


admin.site.register(UserModel, UserAdmin)
