from django.test import TestCase
import json

from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
from Server.serializers import AttractionSerializer, TrackSerializer, UserSerializer, AmericanQuestionSerializer, \
    HintSerializer, FeedbackInstanceSerializer, TripSerializer, GetRelevantPreviousTripInformationSerializer
import random
from django.conf import settings
import math
from enum import Enum


class TrackLength(Enum):
    NOT_EXIST = -1
    EMPTY = 1
    SHORT = 1
    MEDIUM = 2
    LONG = 3


def randomValidNumber(Min, Max):
    while True:
        yield random.random() * Max + Min


def distance(userX, userY, a):
    def haversin(x):
        return math.sin(x / 2) ** 2

    return 2 * math.asin(math.sqrt(
        haversin(a["x"] - userX) +
        math.cos(userX) * math.cos(a["x"]) * haversin(a["y"] - userY)))


def closestAttraction(userX, userY, destinations):
    closest = destinations[0]
    minDistance = distance(userY, userY, destinations[0])
    for dst in destinations[1:]:
        tempDistance = distance(userX, userY, dst)
        if tempDistance < minDistance:
            closest = dst
            minDistance = tempDistance

    return closest


def check_getClosestAttractionFromTrack(track, testCase):
    destinations = testCase.bl.getAllAttractionsFromTrack(track)
    for dst in destinations:
        userX, userY = dst["x"], dst["y"]
        testCase.check(
            closestAttraction(userX, userY, destinations),
            testCase.bl.getClosestAttractionFromTrack(track, userX, userY),
            AttractionSerializer
        )


def check_getTrackAndNextAttractionByLengthAndUserLocation(length, expectedAttraction, possibleTracks, testCase):
    actualTrack, actualAttraction = testCase.bl.getTrackAndNextAttractionByLengthAndUserLocation(
        length,
        expectedAttraction["x"],
        expectedAttraction["y"]
    )
    testCase.assertEqual(expectedAttraction, actualAttraction)
    testCase.assertIn(actualTrack, possibleTracks)


class Unit_BL(TestCase):
    BL_Impl = BL_Implementation()
    BL_Impl.setDAL(DAL_Implementation())
    bl = BLProxy()
    bl.setImplementation(BL_Impl)

    # Users
    UserNotExist = {"id": -1, "name": "NotExist", "socialNetwork": "Test", "lastSeen": None, "email": None}
    UserExist = {"id": 0, "name": "Exist", "socialNetwork": "Test", "lastSeen": None, "email": None}
    UserNew = {"id": 1, "name": "New", "socialNetwork": "Test", "lastSeen": None, "email": None}

    # Attractions
    xGen = randomValidNumber(settings.VALID_SECTOR[0], settings.VALID_SECTOR[1])
    yGen = randomValidNumber(settings.VALID_SECTOR[2], settings.VALID_SECTOR[3])
    AttractionNotExist = {"id": -1, "name": "NotExist", "x": next(xGen), "y": next(yGen), "description": "",
                          "picturesURLS": [], "videosURLS": []}
    AttractionSimple = {"id": 0, "name": "Simple", "x": next(xGen), "y": next(yGen), "description": "",
                        "picturesURLS": [], "videosURLS": []}
    AttractionPicture = {"id": 1, "name": "Simple", "x": next(xGen), "y": next(yGen), "description": "",
                         "picturesURLS": ["x.jpg"], "videosURLS": []}
    AttractionVideo = {"id": 2, "name": "Simple", "x": next(xGen), "y": next(yGen), "description": "",
                       "picturesURLS": [], "videosURLS": ["x.mp4"]}

    # Tracks

    TrackNotExist = {"id": -1, "subTrack": None, "points": [], "length": TrackLength.NOT_EXIST}
    TrackEmpty = {"id": 0, "subTrack": None, "points": [], "length": TrackLength.EMPTY}
    TrackShort = {"id": 1, "subTrack": None, "points": [AttractionSimple], "length": TrackLength.SHORT}
    TrackMedium = {"id": 2, "subTrack": TrackShort, "points": [AttractionPicture], "length": TrackLength.MEDIUM}
    TrackLong = {"id": 3, "subTrack": TrackMedium, "points": [AttractionVideo], "length": TrackLength.LONG}

    # AmericanQuestions
    AQ_NotExist = {"id": -1, "question": "NotExist?", "answers": ["Yes"], "indexOfCorrectAnswer": 0,
                   "attraction": AttractionNotExist}
    AQ_Simple = {"id": 0, "question": "Simple?", "answers": ["Yes", "No"], "indexOfCorrectAnswer": 0,
                 "attraction": AttractionSimple}
    AQ_Picture = {"id": 1, "question": "Picture?", "answers": ["Yes", "No", "No"], "indexOfCorrectAnswer": 0,
                  "attraction": AttractionPicture}
    AQ_Video = {"id": 2, "question": "Video?", "answers": ["Yes", "No", "No", "No"], "indexOfCorrectAnswer": 0,
                "attraction": AttractionPicture}

    # Hints
    Hint_NotExist = {"id": -1, "attraction": AttractionNotExist, "kind": "HintText", "data": "NotExist"}
    Hint_Text = {"id": 0, "attraction": AttractionSimple, "kind": "HintText", "data": "Simple HT"}
    Hint_Picture = {"id": 1, "attraction": AttractionSimple, "kind": "HintPicture", "data": "x.jpg"}
    Hint_Video = {"id": 2, "attraction": AttractionSimple, "kind": "HintVideo", "data": "x.mp4"}
    Hint_Map = {"id": 3, "attraction": AttractionSimple, "kind": "HintMap",
                "data": "" + AttractionSimple["x"] + "," + AttractionSimple["y"]}

    # Feedbacks
    Feedback_NotExist = {"id": -1, "question": "NotExist?", "kind": "FeedbackText"}
    Feedback_Text = {"id": 0, "question": "Text?", "kind": "FeedbackText"}
    Feedback_Rating = {"id": 1, "question": "Rating?", "kind": "FeedbackRating"}

    # Trip
    Trip_NotExist = {"id": -1, "user": UserNotExist, "groupName": "NotExist", "playersAges": [], "score": 0,
                     "track": TrackNotExist, "attractionsDone": []}
    Trip_Empty = {"id": 0, "user": UserExist, "groupName": "ExistEmpty", "playersAges": [10, 11], "score": 0,
                  "track": TrackEmpty, "attractionsDone": []}
    Trip_Short = {"id": 1, "user": UserExist, "groupName": "ExistShort", "playersAges": [10, 11], "score": 300,
                  "track": TrackShort, "attractionsDone": [AttractionSimple]}
    Trip_New = {"id": 2, "user": UserExist, "groupName": "New", "playersAges": [1, 2], "score": 0,
                "track": TrackShort, "attractionsDone": [AttractionSimple]}
    Trip_AddAttraction = {"id": 3, "user": UserExist, "groupName": "Add attraction", "playersAges": [10], "score": 200,
                          "track": TrackMedium, "attractionsDone": [AttractionSimple]}

    # Feedbacks Instances
    FeedbackInstance_NotExist = {"id": -1, "feedback": Feedback_NotExist, "trip": Trip_NotExist, "answer": "NotExist"}
    FeedbackInstance_Text = {"id": 0, "feedback": Feedback_Text, "trip": Trip_Empty, "answer": "Empty and Text"}
    FeedbackInstance_Rating = {"id": 1, "feedback": Feedback_Rating, "trip": Trip_Empty, "answer": "3"}

    def check(self, expected, actual, classSerializer=None, many=False, assertFunc=None):
        jsonActual = None
        if actual is not None:
            serializerActual = classSerializer(actual, many=many)
            jsonActual = json.loads(json.dumps(serializerActual.data))
        if assertFunc is None:
            self.assertEqual(expected, jsonActual)
        else:
            assertFunc(actual, expected)

    def test_getUser_NotExist(self):
        self.check(
            None,
            self.bl.getUser(self.UserNotExist),
            UserSerializer
        )

    def test_getUser_Exist(self):
        self.check(
            self.UserExist,
            self.bl.getUser(self.UserExist),
            UserSerializer
        )

    def test_getPreviousUserTrip_NotExist(self):
        self.check(
            None,
            self.bl.getPreviousUserTrip(self.UserNotExist),
            TripSerializer
        )

    def test_getPreviousUserTrip_Exist(self):
        self.check(
            self.Trip_Short,
            self.bl.getPreviousUserTrip(self.UserExist),
            TripSerializer
        )

    def test_getRelevantPreviousTripInformation_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getPreviousUserTrip(self.UserNotExist)

    def test_getRelevantPreviousTripInformation_New(self):
        self.check(
            None,
            self.bl.getRelevantPreviousTripInformation(self.UserNew),
            GetRelevantPreviousTripInformationSerializer
        )

    def test_getRelevantPreviousTripInformation_Exist(self):
        self.check(
            {"groupName": self.Trip_Short["groupName"], "playersAges": self.Trip_Short["playersAges"]},
            self.bl.getRelevantPreviousTripInformation(self.UserExist),
            GetRelevantPreviousTripInformationSerializer
        )

    def test_getAllAttractionsFromTrack_NotExist(self):
        self.check(
            None,
            self.bl.getAllAttractionsFromTrack(self.TrackNotExist)
        )

    def test_getAllAttractionsFromTrack_Empty(self):
        self.check(
            [],
            self.bl.getAllAttractionsFromTrack(self.TrackEmpty)
        )

    def test_getAllAttractionsFromTrack_Short(self):
        self.check(
            self.TrackShort["points"] + self.bl.getAllAttractionsFromTrack(self.TrackShort["subTrack"]),
            self.bl.getAllAttractionsFromTrack(self.TrackShort)
        )

    def test_getAllAttractionsFromTrack_Medium(self):
        self.check(
            self.TrackMedium["points"] + self.bl.getAllAttractionsFromTrack(self.TrackMedium["subTrack"]),
            self.bl.getAllAttractionsFromTrack(self.TrackMedium)
        )

    def test_getAllAttractionsFromTrack_Long(self):
        self.check(
            self.TrackLong["points"] + self.bl.getAllAttractionsFromTrack(self.TrackLong["subTrack"]),
            self.bl.getAllAttractionsFromTrack(self.TrackLong)
        )

    def test_getClosestAttractionFromTrack_NotExist(self):
        with self.assertRaises(Exception):
            self.bl.getClosestAttractionFromTrack(self.TrackNotExist, next(self.xGen), next(self.yGen))

    def test_getClosestAttractionFromTrack_Empty(self):
        self.check(
            None,
            self.bl.getClosestAttractionFromTrack(self.TrackEmpty, next(self.xGen), next(self.yGen)),
            AttractionSerializer
        )

    def test_getClosestAttractionFromTrack_Short(self):
        userX, userY = next(self.xGen), next(self.yGen)
        self.check(
            closestAttraction(userX, userY, self.bl.getAllAttractionsFromTrack(self.TrackShort)),
            self.bl.getClosestAttractionFromTrack(self.TrackShort, userX, userY),
            AttractionSerializer
        )
        check_getClosestAttractionFromTrack(self.TrackShort, self)

    def test_getClosestAttractionFromTrack_Medium(self):
        check_getClosestAttractionFromTrack(self.TrackMedium, self)

    def test_getClosestAttractionFromTrack_Long(self):
        check_getClosestAttractionFromTrack(self.TrackLong, self)

    def test_getTrackAndNextAttractionByLengthAndUserLocation_NotExist(self):
        self.check(
            None,
            self.bl.getTrackAndNextAttractionByLengthAndUserLocation(TrackLength.NOT_EXIST,
                                                                     next(self.xGen), next(self.yGen))
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Short(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.SHORT,
            self.AttractionSimple,
            [self.TrackShort],
            self
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Medium(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.MEDIUM,
            self.AttractionSimple,
            [self.TrackShort, self.TrackMedium],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.MEDIUM,
            self.AttractionPicture,
            [self.TrackMedium],
            self
        )

    def test_getTrackAndNextAttractionByLengthAndUserLocation_Long(self):
        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            self.AttractionSimple,
            [self.TrackShort, self.TrackMedium, self.TrackLong],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            self.AttractionPicture,
            [self.TrackMedium, self.TrackLong],
            self
        )

        check_getTrackAndNextAttractionByLengthAndUserLocation(
            TrackLength.LONG,
            self.AttractionVideo,
            [self.TrackLong],
            self
        )

    def test_createTrip_NotExist(self):
        inp = {"user": self.UserNotExist, "groupName": "NotExist", "playerAges": [],
               "trackLength": TrackLength.NOT_EXIST, "x": next(self.xGen), "y": next(self.yGen)}
        self.check(
            None,
            self.bl.createTrip(inp),
            TripSerializer
        )

    def test_createTrip_Short(self):
        attraction = self.Trip_New["attractionsDone"][0]
        user = self.Trip_New["user"]
        inp = {"user": user, "groupName": self.Trip_New["groupName"],
               "playerAges": self.Trip_New["playersAges"], "trackLength": self.Trip_New["track"]["trackLength"],
               "x": attraction["x"], "y": attraction["y"]}
        actual = self.bl.createTrip(inp)
        self.check(
            [self.Trip_New],
            actual,
            TripSerializer,
            assertFunc=self.assertIn
        )
        self.check(
            actual,
            self.bl.getPreviousUserTrip(user),
            TripSerializer
        )

    def test_createUser_Exist(self):
        with self.assertRaises(RuntimeError):
            self.bl.createUser(self.UserExist)

    def test_createUser_NotExist(self):
        self.check(
            self.UserNew,
            self.bl.createUser(self.UserNew),
            UserSerializer
        )

    def test_getHints_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getHints(self.AttractionNotExist)

    def test_getHints_Exist_No_Hints(self):
        self.check(
            None,
            self.bl.getHints(self.AttractionVideo),
            HintSerializer,
            True
        )

    def test_getHints_Exist_With_Hints(self):
        self.check(
            [self.Hint_Map, self.Hint_Text, self.Hint_Picture, self.Hint_Video],
            self.bl.getHints(self.AttractionSimple),
            HintSerializer,
            True,
            assertFunc=self.assertCountEqual
        )

    def test_getFeedbacks_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getFeedbacks(self.Trip_NotExist)

    def test_getFeedbacks_Exist_No_Feedbacks(self):
        self.check(
            None,
            self.bl.getFeedbacks(self.Trip_Short),
            FeedbackInstanceSerializer,
            True
        )

    def test_getFeedbacks_Exist_With_Feedbacks(self):
        self.check(
            [self.FeedbackInstance_Text, self.FeedbackInstance_Rating],
            self.bl.getFeedbacks(self.Trip_Empty),
            FeedbackInstanceSerializer,
            True,
            assertFunc=self.assertCountEqual
        )

    def test_getAmericanQuestion_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getAmericanQuestion(self.AttractionNotExist)

    def test_getAmericanQuestion_No_AQ(self):
        self.check(
            None,
            self.bl.getAmericanQuestion(self.AttractionVideo),
            AmericanQuestionSerializer,
            True
        )

    def test_getAmericanQuestion_With_AQ(self):
        self.check(
            [self.AQ_Simple],
            self.bl.getAmericanQuestion(self.AttractionSimple),
            AmericanQuestionSerializer,
            True,
            assertFunc=self.assertCountEqual
        )

    def test_getAttraction_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getAttraction(self.AttractionNotExist)

    def test_getAttraction_Exist(self):
        self.check(
            self.AttractionSimple,
            self.bl.getAttraction(self.AttractionSimple),
            AttractionSerializer,
        )

    def test_getTrip_NotExist(self):
        with self.assertRaises(RuntimeError):
            self.bl.getTrip(self.Trip_NotExist)

    def test_getTrip_Exist(self):
        self.check(
            self.Trip_Short,
            self.bl.getTrip(self.Trip_Short),
            TripSerializer
        )

    def test_signUp_NotExistedUser(self):
        actual = self.bl.signUp(self.UserNew)
        self.check(
            self.UserNew,
            actual,
            UserSerializer
        )
        self.check(
            None,
            actual["lastSeen"],
        )

    def test_signUp_ExistedUser(self):
        actual = self.bl.signUp(self.UserExist)
        self.check(
            self.UserExist,
            actual,
            UserSerializer
        )
        self.check(
            None,
            actual["lastSeen"],
            assertFunc=self.assertNotEquals
        )