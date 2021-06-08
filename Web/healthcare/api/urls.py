from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'appointments', views.AppointmentViewset)
router.register(r'doctors', views.DoctorViewset)
router.register(r'clinic', views.ClinicViewset)
router.register(r'hospitals', views.HospitalViewset)
router.register(r'ambulance', views.AmbulanceViewset)
router.register(r'specialist', (views.SpecialistViewset))

urlpatterns = [
    path('', include(router.urls))
]