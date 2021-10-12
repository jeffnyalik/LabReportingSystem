from django.urls import path
from .import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', views.RegisterApiView.as_view(), name='register-user'),
    path('login/', views.MyObtainTokenPairView.as_view(), name='login-user'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),


    # Facility owner login
    path('staff-login/', views.StaffLoginApiView.as_view(), name='staff-login'),

]