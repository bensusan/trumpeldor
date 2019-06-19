from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_OldTrip(TestCase):

    def test_getPreviousTripByUser_NotExist(self):
        check(
            None,
            dal.getPreviousTripByUser(UserNotExist["name"], UserNotExist["socialNetwork"]),
            self.assertEquals,
            TripSerializer
        )

    def test_getPreviousTripByUser_Exist(self):
        check(
            Trip_Short,
            dal.getPreviousTripByUser(UserExist["name"], UserExist["socialNetwork"]),
            self.assertEquals,
            TripSerializer
        )


class Unit_createTrip(TestCase):

    def test_createTrip_Exist(self):
        check(
            None,
            dal.createTrip(
                Trip_Short["user"], Trip_Short["groupName"], Trip_Short["playersAges"],
                Trip_Short["track"],
                Trip_Short["attractionsDone"][len(Trip_Short["attractionsDone"])-1]),
            self.assertEquals,
            TripSerializer
        )

    def test_createTrip_NotExist(self):
        check(
            Trip_New,
            dal.createTrip( Trip_New["user"], Trip_New["groupName"], Trip_New["playersAges"],
                            Trip_New["track"],
                            Trip_New["attractionsDone"][len(Trip_New["attractionsDone"])-1]),
            self.assertEquals,
            TripSerializer
        )


class Unit_FinishAttraction(TestCase):

    def test_doneAttractionInTrip(self, trip, attraction):
        expected = Trip_AddAttraction.copy()
        dal.doneAttractionInTrip(Trip_AddAttraction, AttractionPicture)
        expected["attractionsDone"] = [AttractionPicture] + expected["attractionsDone"]
        check(expected, Trip_AddAttraction, self.assertEquals)


class Unit_getTrip(TestCase):

    def test_getTrip_NotExist(self):
        check(
            None,
            dal.getTrip(Trip_NotExist["id"]),
            self.assertEquals,
            TripSerializer
        )

    def test_getTrip_Empty(self):
        check(
            Trip_Empty,
            dal.getTrip(Trip_Empty["id"]),
            self.assertEquals,
            TripSerializer
        )

    def test_getTrip_Short(self):
        check(
            Trip_Short,
            dal.getTrip(Trip_Short["id"]),
            self.assertEquals,
            TripSerializer
        )
