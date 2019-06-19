from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_GetAmericanQuestion(TestCase):

    def test_getAmericanQuestion_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getAmericanQuestion(AttractionNotExist)

    def test_getAmericanQuestion_No_AQ(self):
        check(
            None,
            bl.getAmericanQuestion(AttractionVideo),
            self.assertEquals,
            AmericanQuestionSerializer,
            True
        )

    def test_getAmericanQuestion_With_AQ(self):
        check(
            [AQ_Simple],
            bl.getAmericanQuestion(AttractionSimple),
            self.assertCountEqual,
            AmericanQuestionSerializer,
            True
        )
