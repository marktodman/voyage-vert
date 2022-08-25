from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    """Test pages perform as expected"""

    def setUp(self):
        """Set up tests"""
        self.client = Client()
        self.home_url = reverse('home')
        self.routes_url = reverse('routes')

    def test_home_page_loads_correctly(self):
        """ Test home page loads correctly """
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_routes_page_loads_correctly(self):
        """ Test routes page loads correctly """
        response = self.client.get(self.routes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'routes.html')