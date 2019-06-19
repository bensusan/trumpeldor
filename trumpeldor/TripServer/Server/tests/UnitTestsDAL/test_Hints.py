from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getHints(TestCase):

    def test_getHints_NotExist(self):
        check(
            None,
            dal.getHints(AttractionNotExist),
            self.assertEquals,
            HintSerializer,
            True
        )

    def test_getHints_Simple(self):
        check(
            [Hint_Text, Hint_Picture, Hint_Video],
            dal.getHints(AttractionSimple),
            self.assertEquals,
            AttractionSerializer
        )
