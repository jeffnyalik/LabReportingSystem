from django.contrib import admin
from .models import CustomUser, Profile

admin.site.register(Profile)


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'is_active', 'is_fac_staff', 'phone_number', 'city']
    list_editable = ['is_fac_staff', 'is_active', 'phone_number', 'city']
admin.site.register(CustomUser, UserAdmin)