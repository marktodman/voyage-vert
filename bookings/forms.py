from django import forms
from django.forms import ModelForm
from .models import Route, Trip, Booking, Profile
from django.contrib.auth.models import User
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
        labels = {
            'passenger': 'Lead Passenger Username',
            'number_passengers': 'Total Number of Passengers'
        }

    # Disable certain fields that are limited to the user and the trip instance
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['route_name'].disabled = True
        self.fields['passenger'].disabled = True


# Add custom fields to the allauth signup form
class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user

# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    # Disable the username field and remove help text
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['username'].help_text = None


# Profile form
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','sailing_exp']
