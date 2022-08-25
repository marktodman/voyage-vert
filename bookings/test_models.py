from django.test import TestCase
from .models import Route, Trip, Booking, Profile
from django.contrib.auth.models import User


class TestModels(TestCase):
    """Test Model"""

    def setUp(self):
        """Set up test parameters"""
        self.user = User(username='Test_User')
        self.profile = Profile(bio='Test bio')
        self.route = Route(route_name='London to Amsterdam')
        self.trip = Trip(trip_date='2029-03-01')
        self.booking = Booking(
            trip_date=self.trip,
            route_name=self.route,
            passenger=self.user,
            number_passengers=2,
            )

    def test_user_in_user_model(self):
        """Test User Model assigns user"""
        self.assertEqual(self.user.username, 'Test_User')

    def test_bio_in_profile_model(self):
        """Test Profile Model assigns bio"""
        self.assertEqual(self.profile.bio, 'Test bio')

    def test_route_name_in_route_model(self):
        """Test Route Model assigns route name"""
        self.assertEqual(self.route.route_name, 'London to Amsterdam')

    def test_trip_date_in_trip_model(self):
        """Test Rrip Model assigns date"""
        self.assertEqual(self.trip.trip_date, '2029-03-01')

    def test_add_number_passengers_to_booking(self):
        """Test Booking Model records number of passengers"""
        self.assertEqual(self.booking.number_passengers, 2)

    def test_booking_is_created_using_route_trip_and_user_information(self):
        """Test Booking Model uses foreign keys from 
        Route, Trip and User Models"""
        self.assertEqual(self.booking.route_name, self.route)
        self.assertEqual(self.booking.trip_date, self.trip)
        self.assertEqual(self.booking.passenger, self.user)
