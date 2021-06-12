from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length = 100)
    address = forms.CharField(max_length = 100)
    date = forms.DateTimeField()
    doctor_note = forms.CharField(max_length = 100)