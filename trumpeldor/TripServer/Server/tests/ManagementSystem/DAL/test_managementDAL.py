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

    # attraction = {'id': 0, 'name': 'de vinchi', 'x': 32.1111, 'y': 23.43433, 'description': 'bla bla',
    #               'picturesURLS': [], 'videosURLS': []}
    attr = Attraction(id=1, name='de vinchi', x=32.1111, y=23.43433, description='bla bla', picturesURLS=[],
                      videosURLS=[])
    serializerActual = AttractionSerializer(attr, many=False)
    jsonActualAttraction = json.loads(json.dumps(serializerActual.data))

    def test_add_attraction(self):
        self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
        self.assertEqual(True, Attraction.objects.filter(name='de', x=1, y=2,
                                                         description='dsfre', picturesURLS=[], videosURLS=[]).exists())

    def test_add_hint(self):
        attr = self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
        self.dal.add_hint(attr, 'HT', 'some hint in text')
        self.assertEqual(True, Hint.objects.filter(attraction=attr, kind='HT', data='some hint in text').exists())

    def test_add_american_question(self):
        attr = self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
        self.dal.add_american_question(attr, 'are you?', ['yes', 'no'],  1)
        self.assertEqual(True, AmericanQuestion.objects.filter(attraction=attr, question='are you?', answers=['yes', 'no'], indexOfCorrectAnswer=1).exists())




# class DALUnitTestsForDestroying(DALUnitTests):
#
#     def test_delete_attraction(self):
#         self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
#         self.dal.delete_attraction(self.dal.get_attraction_by_x_y(1, 2))
#         self.assertEqual(False, Attraction.objects.filter(name='de', x=1, y=2,
#                                                          description='dsfre', picturesURLS=[], videosURLS=[]).exists())
#
#     def test_delete_hint(self):
#         attr = self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
#         self.dal.add_hint(attr, 'HT', 'some hint in text')
#         self.dal.delete_hint()
#         self.assertEqual(True, Hint.objects.filter(attraction=attr, kind='HT', data='some hint in text').exists())
#
#     def test_add_american_question(self):
#         attr = self.dal.add_attraction('de', 1, 2, 'dsfre', [], [])
#         self.dal.add_american_question(attr, 'are you?', ['yes', 'no'],  1)
#         self.assertEqual(True, AmericanQuestion.objects.filter(attraction=attr, question='are you?', answers=['yes', 'no'], indexOfCorrectAnswer=1).exists())
