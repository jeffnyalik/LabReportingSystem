from django.urls import path
from .import views

urlpatterns = [
    path('facilities/', views.FacilityApiView.as_view(), name='facilities'),
    path('lab/', views.LabApiView.as_view(), name='lab-test'),

    path('facilities/<int:pk>/', views.FacilityDetailApiView.as_view(), name='facilities-detail'),
]