from django.urls import path
from .import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register-user'),
    path('login/', views.TokenObtainPairView.as_view(), name='login-user'),

]