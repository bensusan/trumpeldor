from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getAttraction(TestCase):

    def test_getAttraction_NotExist(self):
        check(
            None,
            dal.getAttraction(AttractionNotExist["id"]),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getAttraction_Simple(self):
        check(
            AttractionSimple,
            dal.getAttraction(AttractionSimple["id"]),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getAttraction_Picture(self):
        check(
            AttractionPicture,
            dal.getAttraction(AttractionPicture["id"]),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getAttraction_Video(self):
        check(
            AttractionVideo,
            dal.getAttraction(AttractionVideo["id"]),
            self.assertEquals,
            AttractionSerializer
        )
