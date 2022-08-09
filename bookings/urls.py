from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('routes', views.RouteList.as_view(), name='routes'),
    path('routes_trips/<route_id>', views.RouteTrips.as_view(), name='route-trips'),
]
