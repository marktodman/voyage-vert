from django import forms
from django.forms import ModelForm
from .models import Route


# Create a new Route
class RouteForm(ModelForm):
    class Meta:
        model = Route
        fields = "__all__"
