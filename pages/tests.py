from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase):

    def test_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
    def about_home_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)        