from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from django.views import View
from healthcare.settings import HEALTHCARE_API_URL as base_url
from .forms import *
from .models import *
import requests

# Create your views here.
from django.views import generic

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class Home(View):

    def get(self, request):
        context = {}
        url = base_url + '/home'
        headers = ''
        response = requests.get(url)
        if response.status_code == 200:
            context = response.json()
            print(context)
        
        return render(request, 'home.html', context)

class DoctorsView(View):
    
    def get(self, request):
        context = {}
        url = base_url + '/doctors'
        headers = ''
        response = requests.get(url)
        if response.status_code == 200:
            doctors = response.json()
            context['doctors'] = doctors
        return render(request, 'doctors.html', context=context)

class SpecialistView(View):
    
    def get(self, request):

        context = {}
        return render(request, 'specialist.html', context)


class ClinicView(View):
    
    def get(self, request):

        context = {}
        return render(request, 'clinic.html', context)

class PrescriptionsView(View):
    
    def get(self, request):

        context = {}
        return render(request, 'prescriptions.html', context = {})

class AppointmentsView(View):

    def get(self, request):

        return render(request, 'appointment.html', context = {})

# TODO BookAppointment Class, BookAmbulance Class
    
class BookAppointmentView(View):

    def get(self, request):

        form = AppointmentForm()
        context = {
            'form': form
        }
        return render(request, 'book_appointment.html', context)

    def post(self, request):

        form = AppointmentForm(request.POST)
        print(form)
        if form.is_valid():
            print(form)
        return redirect('/web/book_appointment/')

class HomeView(View):
    def get(self, request):

        return render(request, 'home_page.html', context = {})