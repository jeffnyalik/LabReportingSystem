from django.contrib import admin
from .models import CustomUser, Profile, Staff

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Staff)