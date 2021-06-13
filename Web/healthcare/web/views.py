from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from rest_framework.views import APIView
from django.views import View
from healthcare.settings import HEALTHCARE_API_URL as base_url
from .forms import *
from .models import *
import requests
import datetime

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
    
    def get(self, request, field):

        context = {}
        url = base_url + '/doctors'
        print(field)
        params = {'field': field}
        response = requests.get(url)
        if response.status_code == 200:
            specialists = response.json()
            context['doctors'] = specialists
            return render(request, 'doctors.html', context)
    
    def post(self, request):
        
        data = request.POST
        print(data)
        url = base_url + '/doctors'
        params = {'field': data['field']}
        response = requests.get(url, params=params)
        if response.status_code == 200:
            specialists = response.json()
            context['doctors'] = specialists
            return render(request, 'doctors.html', context)



class ClinicView(View):
    
    def get(self, request):

        context = {}
        url = base_url + '/clinic'
        headers = ''
        response = requests.get(url)
        if response.status_code == 200:
            clinics = response.json()
            context['clinics'] = clinics
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
        data = request.POST
        appointment = Appointment(name=data['name'], address=data['address'], contact_number=data['phone'], city=data['city'], state=data['state'], doctor_note=data['message'], doctor=Doctor.objects.get(pk = 1),  date= data['date'], time=data['time'], upcoming=True, canceled= False)
        appointment.save()
        return redirect('/book_appointment/')

class SearchView(View):

    def post(self, request):

        category = request.POST['check-box']
        query = request.POST['name']

        if category == 'all':
            url = base_url + '/clinic'
            params = {'search': query}
            response = requests.get(url, params=params)
            if response.status_code == 200: 
                doctors = response.json()
                url1 = base_url + '/doctors'
                params = {'search': query}
                response1 = requests.get(url1, params=params)
                if response1.status_code == 200: 
                    clinics = response1.json()
                    context = {
                        'doctors': doctors,
                        'clinics': clinics
                    }
                    return render(request, 'search.html', context)
        
        elif category == 'clinic':
            url = base_url + '/clinic'
            params = {'search': query}
            response = requests.get(url, params=params)
            if response.status_code == 200: 
                data = response.json()
                context = {'clinics': data}
                return render(request, 'search.html', context)
        else:
            url = base_url + '/doctors'
            params = {'search': query}
            response = requests.get(url, params=params)
            if response.status_code == 200: 
                data = response.json()
                context = {'doctors': data}
                return render(request, 'search.html', context)

class HomeView(View):
    def get(self, request):

        return render(request, 'home_page.html', context = {})