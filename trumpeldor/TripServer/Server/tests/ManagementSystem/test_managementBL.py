from django.conf import settings
from django.test import TestCase
import json

from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
from Server.serializers import *
import random



def randomValidNumber(Min, Max):
    while True:
        yield random.random() * Max + Min


class BLUnitTests(TestCase):
        BL_Impl = BL_Implementation()
        BL_Impl.setDAL(DAL_Implementation())
        bl = BLProxy()
        bl.setImplementation(BL_Impl)

        attraction = {'id': 1, 'name': 'de vinchi', 'x': 32.1111, 'y': 23.43433, 'description': 'bla bla',
                      'picturesURLS': [], 'videosURLS': []}

        def check(self, expected, actual, classSerializer=None, many=False, assertFunc=None):
            jsonActual = None
            if actual is not None:
                serializerActual = classSerializer(actual, many=many)
                jsonActual = json.loads(json.dumps(serializerActual.data))
            if assertFunc is None:
                self.assertEqual(expected, jsonActual)
            else:
                assertFunc(actual, expected)
        #
        # def test_add_attraction(self):
        #     self.check(
        #         self.attraction,
        #         self.bl.add_attraction(self.attraction),
        #         AttractionSerializer
        #     )

        def test_add_hint(self):
            attr = Attraction(id=1, name='de vinchi', x=32.1111, y=23.43433, description='bla bla', picturesURLS=[],
                              videosURLS=[])
            serializerActual = AttractionSerializer(attr, many=False)
            jsonActual = json.loads(json.dumps(serializerActual.data))
            self.bl.add_attraction(jsonActual)
            hint = {'id': 1, 'attraction': attr, 'kind': 'HM', 'data': 'bla bla bla'}

            self.check(
                hint,
                self.bl.add_hint(attr, hint),
                HintSerializer
            )

