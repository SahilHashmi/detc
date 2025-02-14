from django.urls import path
from . import views

urlpatterns = [
    path('detect-vehicles/', views.detect_vehicles_view, name='detect-vehicles'),
    path('detect-license-plate/', views.detect_license_plate_view, name='detect-license-plate'),
    path('detect-all/', views.detect_all_view, name='detect-all'),
]
