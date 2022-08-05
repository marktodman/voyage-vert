from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('routes', views.RouteList.as_view(), name='routes'),
    path('route_trips/<route_id>', views.route_trips, name='route-trips'),
]
