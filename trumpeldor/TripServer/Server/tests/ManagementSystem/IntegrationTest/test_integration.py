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


class IntegrationTests(DALUnitTests):
    #test for adding attraction, adding amrerican question and adding hint
    def test_attr_question_hint(self):
        self.dal.add_attraction('de', 1, 2, 'dsfre','fdfd', 'null', 'null')
        self.assertTrue(Attraction.objects.filter(name='de', x=1, y=2,
                                                         description='dsfre', script='fdfd', picturesURLS=[], videosURLS=[]).exists())

        attr = Attraction.objects.get(name='de', x=1, y=2, description='dsfre', script='script', picturesURLS='null',
                                      videosURLS='null')
        self.dal.add_hint(attr.id, 'HT', 'some hint in text', "")
        self.assertTrue(
            Hint.objects.filter(attraction=attr, kind='HT', data='some hint in text', description="").exists())
