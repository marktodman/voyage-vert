from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View
from .models import Route, Trip, Profile, Booking
from .forms import RouteForm, TripForm, BookingForm, ProfileForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count


# Home Page
class HomePage(TemplateView):
    """Create Home page view"""
    template_name = 'index.html'


# Route View 
class RouteList(ListView):
    """Create Route View"""
    model = Route
    queryset = Route.objects.filter(status=1).order_by('route_name')
    template_name = 'routes.html'


# Trips View
class Trips(View):
    """Create Trips View"""
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


# Account page
@login_required
def profile(request):
    """Create the Account page. Require login to access"""

    if request.user.is_authenticated:
        # Get profile information
        profile = Profile.objects.get(id=request.user.profile.id)

        # Get information for bookings
        user = request.user.id
        my_trips = Booking.objects.filter(passenger=user)

        context = {
            'profile': profile,
            'my_trips': my_trips,
            }

        return render(request, 'profile.html', context)


# Delete User Account
@login_required
def delete_account(request):
    """Authenticated user can delete their account"""

    # This page can only be accessed by an authenticated user
    if request.user.is_authenticated:
        profile = Profile.objects.get(id=request.user.profile.id)
        user = request.user

        # Check that user really wants to delete this route
        if request.method == 'POST':
            user.delete()
            messages.success(request, (
                'Success! Your profile has been deleted from the database'))
            return redirect('home')

        context = {
            'profile': profile,
        }

        return render(request, 'delete_account.html', context)


# Edit Account Information
@login_required 
def edit_account(request):
    """Authenticated user can edit their user information"""

    # This page can only be accessed by an authenticated user
    if request.user.is_authenticated:
        form = UserForm(request.POST or None, instance=request.user)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, (
                'Success! Your information has been updated'))
                return redirect('profile')

        context = {
            'form': form,
            }

        return render(request, 'edit_account.html', context)


# Edit Profile Information
@login_required 
def edit_profile(request):
    """Authenticated user can edit their additional Profile information"""

    # This page can only be accessed by an authenticated user
    if request.user.is_authenticated:
        form = ProfileForm(request.POST or None, instance=request.user.profile)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, (
                'Success! Your additional profile information has been updated'))
                return redirect('profile')

        context = {
            'form': form,
            }

        return render(request, 'edit_profile.html', context)


# Booking request
def booking(request, trip_id):
    """Authenticated user can express interest in a trip and make a booking"""

    if request.user.is_authenticated:
        trip = Trip.objects.get(id=trip_id)
        route_name = trip.route_name
        trip_date = trip.trip_date
        passenger = request.user

        if request.method == "POST":
            form = BookingForm(request.POST, initial={
                'trip_date': trip,
                'route_name': route_name,
                'passenger': passenger,
            })
                
            if form.is_valid():
                form.save()
                messages.success(request, (
                    'Thank you! Your interest was registered.'))
                return redirect('routes')
        else:
            form = BookingForm(initial={
                'trip_date': trip,
                'route_name': route_name,
                'passenger': passenger,
            })

        context = {
            'trip': trip,
            'trip_date': trip_date,
            'route_name': route_name,
            'passenger': passenger,
            'form': form
            }

        return render(request, 'booking.html', context)

    # For non-authenticated users trying to access the page
    else:
        messages.success(request, (
            'You must be signed in to access this page.'))
        return redirect('account_login')


# Edit booking
@login_required
def edit_booking(request, trip_id):
    """Authenticated user can edit one of their expressions of interest"""
    
    if request.user.is_authenticated:
        booking = Booking.objects.get(id=trip_id)
        form = BookingForm(request.POST or None, instance=booking)

        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, (
                    'Your expression of interest has been updated.'))
                return redirect('profile')

        context = {
            'form': form,
            'booking': booking
            }

        return render(request, 'edit_booking.html', context)

    # For non-authenticated users trying to access the page
    else:
        messages.success(request, (
            'You must be signed in to access this page.'))
        return redirect('account_login')


# An authenticated user can delete one of their expressions of interest
@login_required
def delete_booking(request, trip_id):
    """Authenticated user can delete one of their expressions of interest"""

    if request.user.is_authenticated:
        booking = Booking.objects.get(id=trip_id)

        # Check that user really wants to cancel
        if request.method == 'POST':
            booking.delete()
            messages.success(request, (
                'Success! The trip has been deleted from the database'))
            return redirect('profile')

        context = {
                'booking': booking,
                }

        return render(request, 'delete_booking.html', context)

    # For non-authenticated users trying to access the page
    else:
        messages.success(request, (
            'You must be signed in to access this page.'))
        return redirect('account_login')


# Admin Panel
def admin_panel(request):
    """Superuser can view all routes on the database from the frontend"""

    # This page can only be accessed by a superuser
    if request.user.is_superuser:
        routes = Route.objects.all()
        trips = Trip.objects.all()        

        # Number of bookings on each trip
        num_passenger = Trip.objects.annotate(num_pass=Count('booking'))
        ordered_list = num_passenger.order_by('route_name')

        context = {
                'routes': routes,
                'trips': trips,
                'num_passenger': num_passenger,
                'ordered_list': ordered_list,
                }

        return render(request, 'admin_panel.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Add Route
def add_route(request):
    """Superuser can add a route to the database from the frontend"""

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


# Add Trip
def add_trip(request):
    """Superuser can add a trip to the database from the frontend"""

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


# Edit Route
def edit_route(request, route_id):
    """Superuser can edit routes on the database from the frontend"""

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


# Edit Trip
def edit_trip(request, trip_id):
    """Superuser can edit trips on the database from the frontend"""

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

        return render(request, 'edit_trip.html', context)

    # For non-superusers trying to access the page
    else:
        messages.success(request, (
            'Access denied. Please sign in as an admin.'))
        return redirect('home')


# Delete Route
def delete_route(request, route_id):
    """Superuser can delete a Route"""

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


# Delete Trip
def delete_trip(request, trip_id):
    """Superuser can delete a Trip"""

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
