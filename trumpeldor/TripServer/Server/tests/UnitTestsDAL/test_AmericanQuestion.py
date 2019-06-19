from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getAmericanQuestion(TestCase):

    def test_getAmericanQuestion_NotExist(self):
        check(
            None,
            dal.getAmericanQuestion(AQ_NotExist["attraction"]),
            self.assertEquals,
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Simple(self):
        check(
            AQ_Simple,
            dal.getAmericanQuestion(AQ_Simple["attraction"]),
            self.assertEquals,
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Picture(self):
        check(
            AQ_Picture,
            dal.getAmericanQuestion(AQ_Picture["attraction"]),
            self.assertEquals,
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Video(self):
        check(
            AQ_Video,
            dal.getAmericanQuestion(AQ_Video["attraction"]),
            self.assertEquals,
            AmericanQuestionSerializer
        )
