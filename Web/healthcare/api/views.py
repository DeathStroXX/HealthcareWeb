from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from web.models import *
from web.serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Create your views here.

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class DoctorViewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # filterset_fields = ['name', 'experience', 'rating', 'online_payment']
    filter_fields = {
        'name': ['in', 'exact'],
        'experience': ['in', 'exact'],
        'rating': ['in', 'exact'],
        'online_payment': ['exact'],
    }
    search_fields = ['$name', 'about']

class ClinicViewset(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer

class SpecialistViewset(viewsets.ModelViewSet):
    queryset = Specialist.objects.all()
    serializer_class = SpecialistSerializer

class AmbulanceViewset(viewsets.ModelViewSet):
    queryset = Ambulance.objects.all()
    serializer_class = AmbulanceSerializer

class HospitalViewset(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
