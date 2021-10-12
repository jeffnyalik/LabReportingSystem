from rest_framework.permissions import BasePermission,SAFE_METHODS
from rest_framework.response import Response
from rest_framework import status

class IsFacilityOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_fac_staff:
            return True
        return False