from django import forms
from django.forms import ModelForm
from .models import Route, Trip, Booking


# Create a new Route
class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = '__all__'


# Create a new Trip
class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ('trip_date', 'route_name', 'description', 'status')
        widgets = {
			'trip_date': forms.TextInput(attrs=
            {'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
		}


# Create a new Booking
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'