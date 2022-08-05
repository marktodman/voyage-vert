from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Route, Trip


class HomePage(TemplateView):
    template_name = 'index.html'


class RouteList(ListView): 
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'
    paginate_by = 4


def route_trips(request, route_id):
    route = Route.objects.get(id=route_id)
    trips = route.trip_set.all()
    route_name = route.route_name
    route_image = route.featured_image

    context = {
        "trips": trips,
        "route_name": route_name,
        "route_image": route_image,
    }

    return render(request, 'route_trips.html', context=context)
