from itertools import chain

from django.test import TestCase
import json

from Server.DAL.DAL import DALProxy
from Server.DAL.DAL_Implementation import DAL_Implementation
from Server.serializers import *


class DALUnitTests(TestCase):

    DAL_Impl = DAL_Implementation()
    dal = DALProxy()
    dal.setImplementation(DAL_Impl)


class DALUnitTestsForCreating(DALUnitTests):

    def test_add_attraction(self):
        self.dal.add_attraction('de', 1, 2, 'dsfre', 'null', 'null')
        self.assertTrue(Attraction.objects.filter(name='de', x=1, y=2,
                                                         description='dsfre', picturesURLS=[], videosURLS=[]).exists())

    def test_add_feedback_question(self):
        self.dal.add_feedback_question('are you?', 'FR')
        self.assertTrue(Feedback.objects.filter(question='are you?', kind='FR').exists())


class DALUnitTestsOnAttraction(DALUnitTests):

    def setUp(self):
        Attraction.objects.create(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        Attraction.objects.create(name='be', x=3, y=2, description='bla', picturesURLS='null', videosURLS='null')
        Attraction.objects.create(name='ae', x=3, y=3, description='fds', picturesURLS='null', videosURLS='null')

    def test_delete_attraction(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        self.dal.delete_attraction(attr.id)
        self.assertFalse(Attraction.objects.filter(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[]).exists())

    def test_add_hint(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        self.dal.add_hint(attr.id, 'HT', 'some hint in text', "")
        self.assertTrue(Hint.objects.filter(attraction=attr, kind='HT', data='some hint in text', description="").exists())

    def test_add_american_question(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        self.dal.add_american_question(attr.id, 'are you?', ['yes', 'no'],  [1])
        self.assertTrue(AmericanQuestion.objects.filter(attraction=attr, question='are you?', answers=['yes', 'no'],
                                                        indexOfCorrectAnswer=[0]).exists())

    def test_get_attraction(self):
        attr_expected = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        attr_actual = self.dal.get_attraction(attr_expected.id)
        self.assertEquals(attr_expected, attr_actual)

    def test_edit_attraction(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        self.dal.edit_attraction(attr.id, 'de', 2, 2, 'dsfre', 'null', 'null')
        self.assertTrue(Attraction.objects.filter(name='de', x=2, y=2,
                                                  description='dsfre', picturesURLS='null', videosURLS='null').exists())

    # def test_add_track(self):
    #     attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', script='script', picturesURLS='null', videosURLS='null')
    #     attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', script='script2', picturesURLS='null', videosURLS='null')
    #     attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', script='script3', picturesURLS='null', videosURLS='null')
    #     pp1={'id': attr1.id, 'name':'de', 'x':1, 'y':2, 'description':'dsfre', 'script':'script', 'picturesURLS': 'null', 'videosURLS':'null'}
    #     pp2 = {'id': attr2.id, 'name': 'be', 'x': 3, 'y': 2, 'description': 'bla', 'script':'script2', 'picturesURLS': 'null', 'videosURLS': 'null'}
    #     pp3 = {'id': attr3.id, 'name': 'ae', 'x': 3, 'y': 3, 'description': 'fds', 'script':'script3', 'picturesURLS': 'null', 'videosURLS': 'null'}
    #     p1 = {'id':attr1.id}
    #     p2 = {'id': attr2.id}
    #     p3 = {'id': attr3.id}
    #     points = [p1, p2, p3]
    #     self.dal.add_track(None, points, 1)
    #     track = self.dal.get_track_by_length(1)
    #     print(type(track.points))
    #     self.assertTrue(Track.objects.filter(subTrack=None, points=[attr1, attr2, attr3] , length=1).exists())



class DALUnitTestsOnHints(DALUnitTests):

    def setUp(self):
        Attraction.objects.create(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        Hint.objects.create(attraction=attr, kind='HM', data='bla bla bla')

    def test_edit_hint(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        hint = Hint.objects.get(attraction=attr, kind='HM', data='bla bla bla')
        self.dal.edit_hint(attr.id, hint.id, 'another bla', 'ds')
        self.assertTrue(Hint.objects.filter(attraction=attr, kind='HM', data='another bla', description='ds').exists())

    def test_delete_hint(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        hint = Hint.objects.get(attraction=attr, kind='HM', data='bla bla bla')
        self.dal.delete_hint(attr.id, hint.id)
        self.assertFalse(Hint.objects.filter(attraction=attr, kind='HM', data='bla bla bla').exists())

    def test_get_hint(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        hint_expected = Hint.objects.get(attraction=attr, kind='HM', data='bla bla bla')
        hint_actual = self.dal.get_hint(attr.id, hint_expected.id)
        self.assertEquals(hint_expected, hint_actual)


class DALUnitTestsOnAmericanQuestions(DALUnitTests):

    def setUp(self):
        Attraction.objects.create(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        AmericanQuestion.objects.create(attraction=attr, question='are you?',
                                        answers=['yes', 'no'], indexOfCorrectAnswer=[1])
        AmericanQuestion.objects.create(attraction=attr, question='are you2?',
                                        answers=['yes', 'no'], indexOfCorrectAnswer=[2])

    def test_delete_american_question(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        aquestion = AmericanQuestion.objects.get(attraction=attr, question='are you?',
                                        answers=['yes', 'no'], indexOfCorrectAnswer=[1])
        self.dal.delete_american_question(attr.id, aquestion.id)
        self.assertFalse(AmericanQuestion.objects.filter(attraction=attr, question='are you?',
                                        answers=['yes', 'no'], indexOfCorrectAnswer=[1]).exists())

    def test_get_american_question(self):
        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS='null', videosURLS='null')
        aquestion = AmericanQuestion.objects.get(attraction=attr, question='are you?',
                                        answers=['yes', 'no'], indexOfCorrectAnswer=[1])
        self.assertEqual(aquestion, self.dal.get_american_question(attr.id, aquestion.id))




# # class DALUnitTestsOnTrack(DALUnitTests):
# #
# #     def setUp(self):
# #         attr1 = Attraction.objects.create(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.create(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.create(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         Track.objects.create(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #
# #     def test_add_track2(self):
# #         attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         # self.dal.get_track(None, points, 1)
# #         track1 = Track.objects.get(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #         self.assertTrue(Track.objects.filter(subTrack=track1, points=track1.points, length=2).exists())
# #
# #     def test_add_track3(self):
# #         attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         # self.dal.get_track(None, points, 1)
# #         track1 = Track.objects.get(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #         self.assertTrue(Track.objects.filter(subTrack=track1, points=track1.points, length=3).exists())
# #
# #     def test_get_track_by_length(self):
# #         attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         # self.dal.get_track(None, points, 1)
# #         track_expected = Track.objects.get(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #         track_actual = self.dal.get_track_by_length(1)
# #         self.assertEquals(track_expected, track_actual)
# #
# #     def test_delete_track(self):
# #         attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         # self.dal.get_track(None, points, 1)
# #         track = Track.objects.get(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #         self.dal.delete_track(track.id)
# #         self.assertFalse(Track.objects.filter(subTrack=None, points=track.points, length=1).exists())
# #
# #     def test_edit_track(self):
# #         attr1 = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', picturesURLS=[], videosURLS=[])
# #         attr2 = Attraction.objects.get(name='be', x=3, y=2, description='bla', picturesURLS=[], videosURLS=[])
# #         attr3 = Attraction.objects.get(name='ae', x=3, y=3, description='fds', picturesURLS=[], videosURLS=[])
# #         points = list(attr1, attr2)
# #         track = Track.objects.get(subTrack=None, points=list(attr1, attr2, attr3), length=1)
# #         self.dal.edit_track(track.id, points)
# #         self.assertTrue(Track.objects.filter(subTrack=None, points=points, length=1).exists())
# #
