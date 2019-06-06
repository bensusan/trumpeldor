from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_OldTrip(TestCase):
    oldUser = addUserJson(UserExist)
    addAttractionJson(AttractionSimple)
    addTrackJson(TrackShort)
    trip = bl.createTrip(
        {
            "user": UserExist,
            "groupName": Trip_Short["groupName"],
            "playersAges": Trip_Short["playersAges"],
            "trackLength": TrackShort["length"],
            "x": AttractionSimple["x"],
            "y": AttractionSimple["y"]
        })

    newUser = addUserJson(UserNew)

    def test_getPreviousUserTrip_NotExist(self):
        check(
            None,
            bl.getPreviousUserTrip(UserNotExist),
            self.assertEquals,
            TripSerializer
        )

    def test_getPreviousUserTrip_Exist(self):
        check(
            self.trip,
            bl.getPreviousUserTrip(UserExist),
            self.assertEquals
        )

    def test_getRelevantPreviousTripInformation_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getPreviousUserTrip(UserNotExist)

    def test_getRelevantPreviousTripInformation_New(self):
        check(
            None,
            bl.getRelevantPreviousTripInformation(self.newUser),
            self.assertEquals,
            GetRelevantPreviousTripInformationSerializer
        )

    def test_getRelevantPreviousTripInformation_Exist(self):
        check(
            {"groupName": Trip_Short["groupName"], "playersAges": Trip_Short["playersAges"]},
            bl.getRelevantPreviousTripInformation(self.oldUser),
            self.assertEquals,
            GetRelevantPreviousTripInformationSerializer
        )

    def test_createTrip_NotExist(self):
        inp = {"user": UserNotExist, "groupName": "NotExist", "playerAges": [],
               "trackLength": TrackLength.NOT_EXIST.value, "x": next(xGen), "y": next(yGen)}
        self.assertRaises(RuntimeError, bl.createTrip, inp)

