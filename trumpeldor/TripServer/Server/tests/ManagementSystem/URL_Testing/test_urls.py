from django.test import Client, TestCase

from Server.DAL.DAL import *
from Server.DAL.DAL_Implementation import *


class SimpleTestForAttractions(TestCase):
    def setUp(self):
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()
        # Every test needs a client.
        self.client = Client()

    def test_attractions_url(self):
        response = self.client.get('/managementsystem/attrctions/')

        # Check that catches error
        self.assertEqual(response.status_code, 404)

        # Issue a GET request.
        response = self.client.get('/managementsystem/attraction/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Issue a GET request.
        response = self.client.post('/managementsystem/attraction/',
                                    {'name': 'de vinchi', 'x': '32.1111', 'y': '23.43433', 'description': 'bla bla',
                                     'script': 'script', 'picturesURLS': 'null', 'videosURLS': 'null'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)



class SimpleTestForAQ(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()

    def test_details(self):
        response = self.client.post('/managementsystem/attraction/',
                                    {'name': 'de vinchi', 'x': '32.1111', 'y': '23.43433', 'description': 'bla bla',
                                     'script': 'script', 'picturesURLS': 'null', 'videosURLS': 'null'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/managementsystem/attraction/1/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/managementsystem/attraction/1/aquestion/',
                                    {'question': 'stam?', 'answers': '{\'ans1\', \'ans2\', \'ans3\'}',
                                     'indexOfCorrectAnswer': '1'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/managementsystem/attraction/1/aquestion/1/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)


class SimpleTestForHints(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()

    def test_details(self):
        response = self.client.post('/managementsystem/attraction/',
                                    {'name': 'de vinchi', 'x': '453', 'y': '23.3', 'description': 'bla bla',
                                     'script': 'script', 'picturesURLS': 'null', 'videosURLS': 'null'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/managementsystem/attraction/1/hint/',
                                    {'kind': 'HP', 'data': 'image',
                                     'description': 'null'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/managementsystem/attraction/1/hint/1/')
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)



class SimpleTestForFeedback(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()

    def test_details(self):
        response = self.client.post('/managementsystem/feedback/',
                                    {'question': 'stam', 'kind': 'FT'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)




