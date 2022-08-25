from django.test import TestCase, Client
from django.urls import reverse
from .models import Route, Trip
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Test Views perform as expected"""

    def setUp(self):
        """Set up tests"""
        self.client = Client()
        self.home_url = reverse('home')
        self.routes_url = reverse('routes')
        username = "Authenticated_User"
        password = "password7475"
        self.user = User.objects.create_user(
            username=username, password=password)

    def test_home_page_loads_correctly(self):
        """ Test home page loads correctly using correct template"""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_routes_page_loads_correctly(self):
        """ Test routes page loads correctly using correct template"""
        response = self.client.get(self.routes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'routes.html')

    def test_trips_page_loads_correctly(self):
        """ Test trips page loads correctly using correct template"""
        route = Route.objects.create(
            route_name='Test_Name',
            description='Test_Description',
            duration=1,
            distance=2,
            status=1,
        )
        response = self.client.get(f'/trips/{route.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trips.html')

    def test_booking_page_loads_correctly(self):
        """ Test booking page loads correctly using correct template"""
        trip = Trip.objects.create(
            trip_date='2029-03-01',
            description='Test',
            status=1
        )
        self.client.login(
            username="Authenticated_User", password="password7475")
        response = self.client.get(f'/booking/{trip.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')

    def test_booking_page_cannot_be_accessed_unless_user_authenticated(self):
        """Test user must be authenticated to access booking page"""
        trip = Trip.objects.create(
            trip_date='2029-03-01',
            description='Test',
            status=1
        )
        response = self.client.get(f'/booking/{trip.id}')
        self.assertEqual(response.status_code, 302)

    def test_admin_panel_page_cannot_be_accessed_unless_superuser(self):
        """Test user must be superuser to access booking page"""
        response = self.client.get('/admin_panel')
        self.assertEqual(response.status_code, 302)
        self.client.login(
            username="Authenticated_User", password="password7475")
        response = self.client.get('/admin_panel')
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_superuser(
            username="Super_User", password="superpassword")
        self.client.login(
            username="Super_User", password="superpassword")
        response = self.client.get('/admin_panel')
        self.assertEqual(response.status_code, 200)
