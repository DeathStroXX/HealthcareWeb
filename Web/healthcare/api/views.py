from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from web.models import Appointment, Ambulance, Doctor, Specialist, Clinic, Hospital
from rest_framework import views

# Create your views here.

def index(request):

    return HttpResponse('Working fine, Hurray!!!')
