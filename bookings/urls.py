from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('routes', views.RouteList.as_view(), name='routes'),
    path('trips/<route_id>', views.Trips.as_view(), name='trips'),
    path('booking/<trip_id>', views.booking, name='booking'),
    path('add_route', views.add_route, name='add-route'),
    path('add_trip', views.add_trip, name='add-trip'),
    path('admin_panel', views.admin_panel, name='admin-panel'),
    path('edit_route/<route_id>', views.edit_route, name='edit-route'),
    path('edit_trip/<trip_id>', views.edit_trip, name='edit-trip'),
    path('delete_route/<route_id>', views.delete_route, name='delete-route'),
    path('delete_trip/<trip_id>', views.delete_trip, name='delete-trip'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit-profile'),
    path('edit_account/', views.edit_account, name='edit-account'),
    path('delete_account/', views.delete_account, name='delete-account'),
    path('edit_booking/<trip_id>', views.edit_booking, name='edit-booking'),
    path('delete_booking/<trip_id>', views.delete_booking, name='delete-booking'),  # noqa
]
