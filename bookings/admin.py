from django.contrib import admin
from .models import Route, Trip, Passenger


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):

    list_display = ('route_name',)


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')
    search_fields = ['last_name']


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = ('trip_name', 'route_name', 'trip_date')

