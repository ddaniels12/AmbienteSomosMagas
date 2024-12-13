# forms.py
from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'schedule', 'service_type']
        labels = {
            'name': 'Nombre',
            'email': 'Correo Electrónico',
            'phone': 'Teléfono',
            'schedule': 'Horario',
            'service_type': 'Tipo de Servicio',
        }