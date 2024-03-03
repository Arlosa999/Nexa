from django import forms
from .models import Destination, Appointment

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'street', 'city', 'zipcode', 'region', 'country']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'notes']
        widgets = {
            'date_time': forms.DateInput(attrs={'class': 'datepicker'})
        }

