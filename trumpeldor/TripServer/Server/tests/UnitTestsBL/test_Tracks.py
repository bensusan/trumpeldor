from django.test import TestCase
from Server.tests.DataForTests import *
from Server.tests.ServicesForTests import *


class Unit_Test_TracksAttractionsAndUserLocation(TestCase):
    addAttractionJson(AttractionSimple)
    addAttractionJson(AttractionPicture)
    addAttractionJson(AttractionVideo)
    addTrackJson(TrackEmpty)
    addTrackJson(TrackShort)
    addTrackJson(TrackMedium)
    addTrackJson(TrackLong)

    def test_getAllAttractionsFromTrack_NotExist(self):
        check(
            None,
            bl.getAllAttractionsFromTrack(TrackNotExist),
            self.assertEquals
        )

    def test_getAllAttractionsFromTrack_Empty(self):
        check(
            [],
            bl.getAllAttractionsFromTrack(TrackEmpty),
            self.assertEquals
        )

    def test_getAllAttractionsFromTrack_Short(self):
        check(
            TrackShort["points"] + bl.getAllAttractionsFromTrack(TrackShort["subTrack"]),
            bl.getAllAttractionsFromTrack(TrackShort),
            self.assertEquals
        )

    def test_getAllAttractionsFromTrack_Medium(self):
        check(
            TrackMedium["points"] + bl.getAllAttractionsFromTrack(TrackMedium["subTrack"]),
            bl.getAllAttractionsFromTrack(TrackMedium),
            self.assertEquals
        )

    def test_getAllAttractionsFromTrack_Long(self):
        check(
            TrackLong["points"] + bl.getAllAttractionsFromTrack(TrackLong["subTrack"]),
            bl.getAllAttractionsFromTrack(TrackLong),
            self.assertEquals
        )

    def test_getClosestAttractionFromTrack_NotExist(self):
        with self.assertRaises(Exception):
            bl.getClosestAttractionFromTrack(TrackNotExist, next(xGen), next(yGen))

    def test_getClosestAttractionFromTrack_Empty(self):
        check(
            None,
            bl.getClosestAttractionFromTrack(TrackEmpty, next(xGen), next(yGen)),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getClosestAttractionFromTrack_Short(self):
        userX, userY = next(xGen), next(yGen)
        check(
            closestAttraction(userX, userY, bl.getAllAttractionsFromTrack(TrackShort)),
            bl.getClosestAttractionFromTrack(TrackShort, userX, userY),
            self.assertEquals,
            AttractionSerializer
        )
        check_getClosestAttractionFromTrack(TrackShort, self.assertEquals)

    def test_getClosestAttractionFromTrack_Medium(self):
        check_getClosestAttractionFromTrack(TrackMedium, self.assertEquals)

    def test_getClosestAttractionFromTrack_Long(self):
        check_getClosestAttractionFromTrack(TrackLong, self.assertEquals)

    def test_getTrackAndNextAttractionByLengthAndUserLocation_NotExist(self):
        check(
            None,
            bl.getTrackAndNextAttractionByLengthAndUserLocation(
                TrackLength.NOT_EXIST,
                next(xGen),
                next(yGen)
            ),
            self.assertEquals
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Short(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.SHORT,
            AttractionSimple,
            [TrackShort],
            self
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Medium(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.MEDIUM,
            AttractionSimple,
            [TrackShort, TrackMedium],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.MEDIUM,
            AttractionPicture,
            [TrackMedium],
            self
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Long(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            AttractionSimple,
            [TrackShort, TrackMedium, TrackLong],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            AttractionPicture,
            [TrackMedium, TrackLong],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            AttractionVideo,
            [TrackLong],
            self
        )