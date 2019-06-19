from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_GetAttractions(TestCase):

    def test_getAttraction_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getAttraction(AttractionNotExist)

    def test_getAttraction_Exist(self):
        check(
            AttractionSimple,
            bl.getAttraction(AttractionSimple),
            self.assertEquals,
            AttractionSerializer
        )
