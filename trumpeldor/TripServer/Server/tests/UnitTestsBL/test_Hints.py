from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_GetHints(TestCase):

    def test_getHints_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getHints(AttractionNotExist)

    def test_getHints_Exist_No_Hints(self):
        check(
            None,
            bl.getHints(AttractionVideo),
            self.assertEquals,
            HintSerializer,
            True
        )

    def test_getHints_Exist_With_Hints(self):
        check(
            [Hint_Text, Hint_Picture, Hint_Video],
            bl.getHints(AttractionSimple),
            self.assertCountEqual,
            HintSerializer,
            True
        )
