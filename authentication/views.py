from django.shortcuts import render
from rest_framework import generics
from serializers.auth.registerSerializer import RegisterSerializer
from authentication.models import CustomUser
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from serializers.auth.TokenSerailzer import MyTokeObtainPairSerializer


class RegisterApiView(generics.CreateAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokeObtainPairSerializer