from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('routes', views.RouteList.as_view(), name='routes'),
    path('trips/<route_id>', views.Trips.as_view(), name='trips'),
    # path('booking/<trip.id>'), views.Booking.as_view(), name='booking'),
]
