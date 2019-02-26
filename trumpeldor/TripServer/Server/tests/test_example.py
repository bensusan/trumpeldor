from django.test import Client, TestCase

from Server.DAL.DAL import *
from Server.DAL.DAL_Implementation import *


class SimpleTestForAttractions(TestCase):
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
        response = self.client.post('/managementsystem/attractions/',
                                    {'name': 'de vinchi', 'x': '32.1111', 'y': '23.43433', 'description': 'bla bla',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # response = self.client.post('/managementsystem/attractions/',
        #                             {})
        #
        # # Check that the response is 200 OK.
        # self.assertEqual(response.status_code, 422)


class SimpleTestForUsers(TestCase):
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
                                    {'name': 'Itzhak', 'socialNetwork': 'facebook', 'lastSeen': 'null',
                                     'email': 'null'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
        response = self.dal_prox.getUser("Itzhak", "facebook")
        user = User(1)
        # Check that the response is 200 OK.
        self.assertEqual(response, user)


class SimpleTestForAQ(TestCase):
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
                                     'description': 'bla bla',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        attr = Attraction(1)
        response = self.dal_prox.getAmericanQuestion(attr)
        self.assertEqual(response, None)



        response = self.client.post('/usersystem/getAmericanQuestion/',
                                    {'id': '1', 'question': 'stam?', 'answers': '{\'ans1\': \'ans1\'}',
                                     'indexOfCorrectAnswer': 1})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        aq = AmericanQuestion(1)
        response = self.dal_prox.getAmericanQuestion(attr)
        self.assertEqual(response, aq)



class SimpleTestForFeedback(TestCase):
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
                                     'description': 'bla bla',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        attr = Attraction(1)
        response = self.dal_prox.getFeedbacks(attr)
        self.assertEqual(response, None)

        response = self.client.post('/usersystem/getFeedbacks/',
                                    {'id':'1', 'question':'had fun?', 'kind':'text'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        feedb = Feedback(1)
        response = self.dal_prox.getFeedbacks(attr)
        self.assertEqual(response, feedb)

        response = self.client.post('/usersystem/getFeedbacs/',
                                    {'id': '1', 'question': 'had fun?', 'kind': 'text'})
        # for object that doesnt exist
        self.assertEqual(response.status_code, 404)


class SimpleTestForTrack(TestCase):
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
                                     'description': 'bla bla',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        attr = Attraction(1)
        response = self.dal_prox.getAmericanQuestion(attr) # need to be get_track
        self.assertEqual(response, None)

        response = self.client.post('/usersystem/getTrackAndNextAttractionByLengthAndUserLocation/',
                                    {'id': '1', 'subTrack': '', 'points': '{(x:323,y:2314),(x:332,y:3333)}',
                                     'length': '132'})

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        tr = Track(1)
        response = self.dal_prox.get_track(attr)
        self.assertEqual(response, tr)

        response = self.client.post('/usersystem/notrealllll/',
                                    {'id': '1', 'subTrack': '', 'points': '{(x:323,y:2314),(x:332,y:3333)}',
                                     'length': '132'})

        # for object that doesnt exist
        self.assertEqual(response.status_code, 404)


class SimpleTestForHint(TestCase):
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
                                     'description': 'bla bla',
                                     'picturesURLS': '{}', 'videosURLS': '{}'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        attr = Attraction(1)
        response = self.dal_prox.getHints(attr)
        self.assertEqual(response, None)

        response = self.client.post('/usersystem/getHints/',
                                    {'id': '1', 'kind': 'text', 'data': 'this is a hint!'})
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        the_hint = Hint(1)
        response = self.dal_prox.getHints(attr)
        self.assertEqual(response, the_hint)

        response = self.client.post('/usersystem/getHints/',
                                    {'id': '1', 'subTrack': '', 'points': '{(x:323,y:2314),(x:332,y:3333)}',
                                     'length': '132'})
        # for object that doesnt exist because of unmatching fields
        self.assertEqual(response.status_code, 404)
