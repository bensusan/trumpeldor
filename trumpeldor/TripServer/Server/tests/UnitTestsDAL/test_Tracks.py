from django.test import TestCase
from Server.tests.ServicesForTests import *
from Server.tests.DataForTests import *


class Unit_getTrack(TestCase):

    def test_getTrackById_NotExist(self):
        check(
            None,
            dal.getTrackById(TrackNotExist["length"]),
            self.assertEquals,
            TrackSerializer
        )

    def test_getTrackById_EmptyTrack(self):
        check(
            TrackEmpty,
            dal.getTrackById(TrackEmpty["length"]),
            self.assertEquals,
            TrackSerializer
        )

    def test_getTrackById_ShortTrack(self):
        check(
            TrackShort,
            dal.getTrackById(TrackShort["id"]),
            self.assertEquals,
            TrackSerializer
        )

    def test_getTrackById_MediumTrack(self):
        check(
            TrackMedium,
            dal.getTrackById(TrackMedium["id"]),
            self.assertEquals,
            TrackSerializer
        )

    def test_getTrackById_LongTrack(self):
        check(
            TrackLong,
            dal.getTrackById(TrackLong["id"]),
            self.assertEquals,
            TrackSerializer
        )

    def test_getTracksWithSameLength_NotExist(self):
        check(
            None,
            dal.getTracksWithSameLength(-1),
            self.assertEquals,
            TrackSerializer,
            True
        )

    def test_getTracksWithSameLength_Exist(self):
        check(
            [TrackEmpty, TrackShort],
            dal.getTracksWithSameLength(1),
            self.assertEquals,
            TrackSerializer,
            True
        )
