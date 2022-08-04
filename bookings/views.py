from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Route


class HomePage(TemplateView):
    template_name = 'index.html'


class RouteList(ListView):
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'
    paginate_by = 4
