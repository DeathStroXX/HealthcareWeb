from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name = 'signup'),
    path('book_appointment/', views.BookAppointmentView.as_view() , name = 'bookappointment' ),
    path('', views.HomeView.as_view()),
    path('doctors/', views.DoctorsView.as_view()),
    path('clinic/', views.ClinicView.as_view()),
    path('appointments/', views.AppointmentsView.as_view()),
    path('specialist/<str:field>', views.SpecialistView.as_view()),
    path('prescriptions/', views.PrescriptionsView.as_view()),
    path('all/', views.SearchView.as_view()),
]