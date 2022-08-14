from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, View
from .models import Route, Trip
from .forms import RouteForm, TripForm
from django.http import HttpResponseRedirect


class HomePage(TemplateView):
    template_name = 'index.html'


class RouteList(ListView): 
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'
    paginate_by = 4


class Trips(View):

    def get(self, request, route_id, *args, **kwargs):
        queryset = Route.objects.filter(status=1)
        route = get_object_or_404(queryset, id=route_id)
        trips = route.trip_set.all()
        route_name = route.route_name
        route_image = route.featured_image

        context = {
            "trips": trips,
            "route_name": route_name,
            "route_image": route_image,
            }

        return render(request, 'trips.html', context=context)


def add_route(request):
    submitted = False

    if request.method == "POST":
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_route?submitted=True')
    else:
        form = RouteForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
        }

    return render(request, 'add_route.html', context=context)


def add_trip(request):
    submitted = False

    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_trip?submitted=True')
    else:
        form = TripForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted
        }

    return render(request, 'add_trip.html', context=context)