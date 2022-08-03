from django.contrib import admin
from .models import Route, Trip, Passenger, Booking


admin.site.register(Route)

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')
    search_fields = ['last_name']


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = ('route_name', 'trip_date')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('route_name', 'trip_date')
