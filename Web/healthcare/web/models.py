from django.db import models
from django.db.models.base import Model
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 100)
    field = models.CharField(max_length = 100)
    experience = models.IntegerField()
    about = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    consultation_fees = models.IntegerField()
    rating = models.IntegerField()
    available = models.BooleanField(default=True)
    online_payment = models.BooleanField(default=True)

class Clinic(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    ambulance_count = models.IntegerField()

class Ambulance(models.Model):
    type = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class Appointment(models.Model):
    date = models.CharField(max_length = 100, default="")
    time = models.CharField(max_length = 100, default="")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user_id = models.CharField(max_length = 100, default="1")
    upcoming = models.BooleanField(default=True)
    canceled = models.BooleanField(default=False)
    name = models.CharField(max_length = 100, default="")
    address = models.CharField(max_length = 100, blank=False, null=False, default="")
    contact_number = models.CharField(max_length = 100, null=False, default="")
    city = models.CharField(max_length = 100, null=False, default="")
    state = models.CharField(max_length = 100, null=False, default="")
    doctor_note = models.CharField(max_length = 100, default="")

class Specialist(models.Model):
    name = models.CharField(max_length=100)
    doctors = ManyToManyField(Doctor)   




    

