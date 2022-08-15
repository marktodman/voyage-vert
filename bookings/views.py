from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, View
from .models import Route, Trip
from .forms import RouteForm, TripForm
from django.http import HttpResponseRedirect


# Render Home Page
class HomePage(TemplateView):
    template_name = 'index.html'


# Create Route Views 
class RouteList(ListView): 
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'
    paginate_by = 4


# Create Trips Views
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


# Superuser can view all routes on the database from the frontend
def admin_panel(request):
    routes = Route.objects.all()

    context = {
            "routes": routes,
            }

    return render(request, 'admin_panel.html', context=context)


# Superuser can add a route to the database from the frontend
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


# Superuser can add a trip to the database from the frontend
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


# Superuser can edit routes on the database from the frontend
def edit_route(request, route_id):
    route = Route.objects.get(pk=route_id)

    context = {
            "route": route,
            }

    return render(request, 'edit_route.html', context=context)
    