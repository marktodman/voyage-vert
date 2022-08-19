from django import forms
from django.forms import ModelForm
from .models import Route, Trip, Booking
from allauth.account.forms import SignupForm


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


class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user