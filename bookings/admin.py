from django.contrib import admin
from .models import Route, Trip, Booking, Profile


admin.site.register(Route)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):

    list_display = ('route_name', 'trip_date')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('passenger', 'route_name', 'trip_date')
    ordering = ('passenger',)
    search_fields = ('passenger', 'route_name')
    list_filter = ('passenger', 'route_name', 'trip_date')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user',)
