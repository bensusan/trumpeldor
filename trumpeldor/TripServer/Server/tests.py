from django.test import TestCase

# Create your tests here.

import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()
        # response = c.post('/login/', {'username': 'john', 'password': 'smith'})
        # >> > response.status_code

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/managementsystem/attractions/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Issue a GET request.
        response = self.client.post('/managementsystem/attractions/', {'name': 'de vinchi', 'x': '32.1111', 'y': '23.43433', 'description' :'need to work harder',
                                                                       'picturesURLS': '{}', 'videosURLS': '{}'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # response = self.client.post('/managementsystem/attractions/',
        #                             {})
        #
        # # Check that the response is 200 OK.
        # self.assertEqual(response.status_code, 422)
