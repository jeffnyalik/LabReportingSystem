from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers.facilities.facilitySerializer import FacilitySerializer, LabSerializer
from .models import Facility
from lab_test.models import LabTest
from rest_framework import permissions
import json
from django.http import HttpResponse


class FacilityApiView(APIView):
    def get(self, request, format=None):
        facility = Facility.objects.all()
        serializer = FacilitySerializer(facility, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LabApiView(APIView):
    def get(self, request, format=None):
        lab = LabTest.objects.all()
        serializer = LabSerializer(lab, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FacilityDetailApiView(APIView):
    def get(self, request, format=None, pk=None):
        fac = get_object_or_404(Facility, pk=pk)
        serializer = FacilitySerializer(fac)
        return Response(serializer.data, status=status.HTTP_200_OK)

        