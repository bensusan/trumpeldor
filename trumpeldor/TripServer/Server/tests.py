import null
from django.test import TestCase

# Create your tests here.

import unittest
from django.test import Client

from Server.DAL.DAL import *
from Server.DAL.DAL_Implementation import *



class SimpleTestForAttractions(unittest.TestCase):
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

class SimpleTestForUsers(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.dal_prox.getUser("Itzhak", "facebook")

        # Check that the response is 200 OK.
        self.assertEqual(response, None)

        response = self.client.post('/usersystem/signUp/',
                                    {'name': 'Itzhak', 'socialNetwork': 'facebook', 'lastSeen': 'null', 'email': 'null'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = self.dal_prox.getUser("Itzhak", "facebook")
        user = User(1)
        # Check that the response is 200 OK.
        self.assertEqual(response, user)


class SimpleTestForAQ(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.dal_abst = DAL_Abstract()
        self.dal_prox = DALProxy()
        self.dal_impl = DAL_Implementation()
        self.dal_prox.setImplementation(self.dal_impl)
        self.client = Client()

    def test_details(self):

        response = self.client.post('/managementsystem/attractions/',
                                    {'name': 'de vinchi', 'x': '32.1111', 'y': '23.43433',
                                     'description': 'need to work harder',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})
        attr = Attraction(1)
        response = self.dal_prox.getAmericanQuestion(attr)
        self.assertEqual(response, None)

        response = self.client.post('/usersystem/getAmericanQuestion/',
                                    {'id': '1', 'question': 'stam?', 'answers': '{\'ans1\': \'ans1\'}', 'indexOfCorrectAnswer': 1})
        aq = AmericanQuestion(1)
        response = self.dal_prox.getAmericanQuestion(attr)
        self.assertEqual(response, aq)
