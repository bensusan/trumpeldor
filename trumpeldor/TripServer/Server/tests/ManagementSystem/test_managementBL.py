from django.conf import settings
from django.test import TestCase
import json

from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
from Server.serializers import *
import random




class BLUnitTests(TestCase):
        BL_Impl = BL_Implementation()
        BL_Impl.setDAL(DAL_Implementation())
        bl = BLProxy()
        bl.setImplementation(BL_Impl)

        # attraction = {'id': 1, 'name': 'de vinchi', 'x': 32.1111, 'y': 23.43433, 'description': 'bla bla',
        #               'picturesURLS': [], 'videosURLS': []}
        attr = Attraction(id=1, name='de vinchi', x=32.1111, y=23.43433, description='bla bla', picturesURLS=[],
                          videosURLS=[])
        serializerActual = AttractionSerializer(attr, many=False)
        jsonActualAttraction = json.loads(json.dumps(serializerActual.data))

        def check(self, expected, actual, classSerializer=None, many=False, assertFunc=None):
            jsonActual = None
            if actual is not None:
                serializerActual = classSerializer(actual, many=many)
                jsonActual = json.loads(json.dumps(serializerActual.data))
            if assertFunc is None:
                self.assertEqual(expected, jsonActual)
            else:
                assertFunc(actual, expected)

        # def test_add_attraction(self):
        #     self.bl.add_attraction(self.jsonActualAttraction)
        #
        #     self.check(
        #         self.attr,
        #         self.bl.add_attraction(self.attr),
        #         AttractionSerializer
        #     )
        #
        #
        def test_add_hint(self):

            self.bl.add_attraction(self.jsonActualAttraction)
            hint = {'id': 1, 'attraction': self.attr, 'kind': 'HM', 'data': 'bla bla bla'}

            self.check(
                hint,
                self.bl.add_hint(self.attr, hint),
                HintSerializer
            )
        #

        def test_fail_add_hint(self):

            self.bl.add_attraction(self.jsonActualAttraction)
            hint = {'id': 1, 'attraction': self.attr, 'kind': 'HM', 'data': 'bla bla bla'}
            hint2 = {'id': 2, 'attraction': self.attr, 'kind': 'HM', 'data': 'sfdaf bla'}

            self.check(
                hint2,
                self.bl.add_hint(self.attr, hint),
                HintSerializer
            )
        #

        def test_add_american_question(self):
            # self.bl.add_attraction(self.jsonActualAttraction)
            american_q = {'id': 1, 'question': 'alien?', 'answers': ['Yes'],
                          'indexOfCorrectAnswer': 0, 'attraction': self.attr}

            self.check(
                american_q,
                self.bl.add_american_question(self.attr, american_q),
                AmericanQuestionSerializer
            )

        #
        # # def test_fail_add_american_question(self):
        # #
        # #     self.bl.add_attraction(self.jsonActualAttraction)
        # #     american_q = {'id': 1, 'question': 'are you an alien?', 'answers': ["Yes", "No"],
        # #                   'indexOfCorrectAnswer': 1, 'attraction': self.attr}
        # #     american_q2 = {'id': 1, 'question': 'what?', 'answers': ["wow", "wiii"],
        # #                   'indexOfCorrectAnswer': 0, 'attraction': self.attr}
        # #
        # #     self.check(
        # #         american_q2,
        # #         self.bl.add_american_question(self.attr, american_q),
        # #         AmericanQuestionSerializer
        # #     )


        # def test_add_track(self):
        #     self.bl.add_attraction(self.jsonActualAttraction)
        #     some_track = {'id': 1, 'subTrack': None, 'points': [self.attr], 'length': 1}
        #
        #     self.check(
        #         some_track,
        #         self.bl.add_track(some_track),
        #         TrackSerializer
        #     )
        #
        # # def test_fail_add_track(self):
        # #     self.bl.add_attraction(self.jsonActualAttraction)
        # #     some_track = {'id': 1, 'subTrack': None, 'points': [self.attr], 'length': 1}
        # #     some_other_track = {'id': 1, 'subTrack': None, 'points': [], 'length': 0}
        # #
        # #     self.check(
        # #         some_other_track,
        # #         self.bl.add_track(some_track),
        # #         TrackSerializer
        # #     )
        #
        #
        # def test_add_feedback_question(self):
        #     fb = {'id': 1, 'question': 'How was the game?', 'kind': 'FT'}
        #
        #     self.check(
        #         fb,
        #         self.bl.add_feedback_question('How was the game?', 'FT'),
        #         FeedbackSerializer
        #     )
        #
        # # def test_fail_add_feedback_question(self):
        # #     fb = {'id': 1, 'question': 'How was the game?', 'kind': 'FT'}
        # #     fb2 = {'id': 1, 'question': '???', 'kind': 'FR'}
        # #
        # #     self.check(
        # #         fb2,
        # #         self.bl.add_feedback_question('How was the game?', 'FT'),
        # #         FeedbackSerializer
        # #     )
        #
        # def test_get_track(self):
        #     self.bl.add_attraction(self.jsonActualAttraction)
        #     some_track = {'id': 1, 'subTrack': None, 'points': [self.attr], 'length': 1}
        #
        #     self.check(
        #         some_track,
        #         self.bl.get_track(some_track),
        #         TrackSerializer
        #     )


        # def test_get_attraction(self):
        #     self.bl.add_attraction(self.jsonActualAttraction)
        #
        #     self.check(
        #         self.attr,
        #         self.bl.get_attraction(self.attr),
        #         TrackSerializer
        #     )

