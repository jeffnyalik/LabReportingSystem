from django.contrib import admin
from .models import Facility


class FacilityAdmin(admin.ModelAdmin):
    list_display  = ['staff', 'name', 'email', 'contactNumber']
admin.site.register(Facility, FacilityAdmin)