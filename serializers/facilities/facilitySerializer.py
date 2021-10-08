from rest_framework import serializers
from facilities.models import Facility
from lab_test.models import LabTest

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTest
        fields = [
            'id',
            'testName', 
            'price',
            'image',
            'active_status'
        ]


class FacilitySerializer(serializers.ModelSerializer):
    lab_test = LabSerializer(many=True, read_only=True)
    class Meta:
        fields = [
            'id',
            'name',
            'email',
            'image',
            'contactNumber',
            'website',
            'lab_test'
        ]
        model = Facility