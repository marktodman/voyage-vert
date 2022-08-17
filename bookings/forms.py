from django import forms
from django.forms import ModelForm
from .models import Route, Trip


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
