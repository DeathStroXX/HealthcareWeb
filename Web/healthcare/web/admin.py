from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Ambulance)
admin.site.register(Doctor)
admin.site.register(Specialist)
admin.site.register(Clinic)
