from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View
from .models import Route, Trip
from .forms import RouteForm, TripForm, BookingForm
from django.http import HttpResponseRedirect
from django.contrib import messages



# Render Home Page
class HomePage(TemplateView):
    template_name = 'index.html'


# Create Route View 
class RouteList(ListView): 
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'
    paginate_by = 6


# Create Trips View
class Trips(View):

    def get(self, request, route_id, *args, **kwargs):
        queryset = Route.objects.filter(status=1)
        route = get_object_or_404(queryset, id=route_id)
        trips = route.trip_set.filter(status=1)
        route_name = route.route_name
        route_image = route.featured_image

        context = {
            'trips': trips,
            'route_name': route_name,
            'route_image': route_image,
            }

        return render(request, 'trips.html', context)


# An authenticated user can express an interest in a trip
def booking(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    route_name = trip.route_name

    submitted = False

    if request.method == "POST":
        form = BookingForm(request.POST, initial={
            'trip_date': trip,
            'route_name': route_name,
        })
            
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('booking?submitted=True')
    else:
        form = BookingForm(initial={
            'trip_date': trip,
            'route_name': route_name,
        })
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'trip': trip,
        'route_name': route_name,
        'form': form
        }

    return render(request, 'booking.html', context)


# Superuser can view all routes on the database from the frontend
def admin_panel(request):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        routes = Route.objects.all()
        trips = Trip.objects.all()

        context = {
                'routes': routes,
                'trips': trips,
                }

        return render(request, 'admin_panel.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can add a route to the database from the frontend
def add_route(request):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        submitted = False

        if request.method == "POST":
            form = RouteForm(request.POST, request.FILES)
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

        return render(request, 'add_route.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can add a trip to the database from the frontend
def add_trip(request):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
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

        return render(request, 'add_trip.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can edit routes on the database from the frontend
def edit_route(request, route_id):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        route = Route.objects.get(id=route_id)
        if request.method == 'POST':
            form = RouteForm(request.POST, request.FILES, instance=route)

            if form.is_valid():
                form.save()
                messages.success(request, (
                    'Success! Your changes have been saved to the database'))
                return redirect('admin-panel')

        form = RouteForm(instance=route)
        context = {
            'route': route,
            'form': form,
            }

        return render(request, 'edit_route.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can edit trips on the database from the frontend
def edit_trip(request, trip_id):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        trip = Trip.objects.get(id=trip_id)
        form = TripForm(request.POST or None, instance=trip)
        if form.is_valid():
            form.save()
            messages.success(request, (
                'Success! Your changes have been saved to the database'))
            return redirect('admin-panel')

        context = {
                'trip': trip,
                'form': form,
                }

        return render(request, 'edit_trip.html', context=context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can delete a Route
def delete_route(request, route_id):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        route = Route.objects.get(id=route_id)

        # Check that user really wants to delete this route
        if request.method == 'POST':
            route.delete()
            messages.success(request, (
                'Success! The route has been deleted from the database'))
            return redirect('admin-panel')

        context = {
                'route': route
                }

        return render(request, 'delete_route.html', context)

# For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Superuser can delete a Trip
def delete_trip(request, booking_id):

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        trip = Trip.objects.get(id=trip_id)

        # Check that user really wants to delete this trip
        if request.method == 'POST':
            trip.delete()
            messages.success(request, (
                'Success! The trip has been deleted from the database'))
            return redirect('admin-panel')

        context = {
                'trip': trip
                }

        return render(request, 'delete_trip.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


