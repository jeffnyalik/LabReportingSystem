from django.contrib import admin
from .models import Facility, FacilityAdmin, FacilityStaff


admin.site.register(Facility)
admin.site.register(FacilityAdmin)
admin.site.register(FacilityStaff)