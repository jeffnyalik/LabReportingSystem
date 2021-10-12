from django.shortcuts import render
from rest_framework import generics
from serializers.auth.registerSerializer import RegisterSerializer
from authentication.models import CustomUser
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from serializers.auth.TokenSerailzer import MyTokeObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from serializers.auth.customSerializer import CustomLoginSerializer
from django.contrib.auth import authenticate, login
from .models import FacilityUser
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterApiView(generics.CreateAPIView):
    permissions_classes = [permissions.AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
    serializer_class = MyTokeObtainPairSerializer


class StaffLoginApiView(APIView):
    def post(self, request, format=None):
        data = request.data
        email = data['email']
        password = data['password']

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_authenticated and user.is_fac_staff:
                accessToken = RefreshToken.for_user(user)
                access = accessToken.access_token
                refresh = accessToken

                return Response({
                    'access': str(access),
                    'refresh': str(refresh)
                })
                
        else:
            return Response({'error': 'Invalid email password'})
        return Response({'Error': 'User does not exist'})