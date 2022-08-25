from django.test import TestCase, Client
from django.urls import reverse
from .models import Route, Trip
from django.contrib.auth.models import User


class TestViews(TestCase):
    """Test pages perform as expected"""

    def setUp(self):
        """Set up tests"""
        self.client = Client()
        self.home_url = reverse('home')
        self.routes_url = reverse('routes')
        username = "Test_User"
        password = "cardtreewindow7475"
        self.user = User.objects.create_user(
            username=username, password=password)
        self.client.login(username=username, password=password)
        self.route = Route(route_name='London to Amsterdam')
        

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
        username = "Test_User"
        password = "cardtreewindow7475"
        self.client.login(username=username, password=password)
        response = self.client.get(f'/booking/{trip.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')
