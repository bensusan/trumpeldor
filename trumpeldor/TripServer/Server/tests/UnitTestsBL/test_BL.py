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
from Server.Services import *

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


def check_getClosestAttractionFromTrack(track, assertFunc):
    destinations = bl.getAllAttractionsFromTrack(track)
    for dst in destinations:
        userX, userY = dst["x"], dst["y"]
        check(
            closestAttraction(userX, userY, destinations),
            bl.getClosestAttractionFromTrack(track, userX, userY),
            assertFunc,
            AttractionSerializer
        )


def check_getTrackAndNextAttractionByLengthAndUserLocation(length, expectedAttraction, possibleTracks, testCase):
    actualTrack, actualAttraction = bl.getTrackAndNextAttractionByLengthAndUserLocation(
        length,
        expectedAttraction["x"],
        expectedAttraction["y"]
    )
    testCase.assertEqual(expectedAttraction, actualAttraction)
    testCase.assertIn(actualTrack, possibleTracks)


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

TrackNotExist = {"id": -1, "subTrack": None, "points": [], "length": TrackLength.NOT_EXIST.value}
TrackEmpty = {"id": 0, "subTrack": None, "points": [], "length": TrackLength.EMPTY.value}
TrackShort = {"id": 1, "subTrack": None, "points": [AttractionSimple], "length": TrackLength.SHORT.value}
TrackMedium = {"id": 2, "subTrack": TrackShort, "points": [AttractionPicture], "length": TrackLength.MEDIUM.value}
TrackLong = {"id": 3, "subTrack": TrackMedium, "points": [AttractionVideo], "length": TrackLength.LONG.value}

# AmericanQuestions
AQ_NotExist = {"id": -1, "question": "NotExist?", "answers": ["Yes"], "indexOfCorrectAnswer": 0,
               "attraction": AttractionNotExist}
AQ_Simple = {"id": 0, "question": "Simple?", "answers": ["Yes", "No"], "indexOfCorrectAnswer": 0,
             "attraction": AttractionSimple}
AQ_Picture = {"id": 1, "question": "Picture?", "answers": ["Yes", "No", "No"], "indexOfCorrectAnswer": 0,
              "attraction": AttractionPicture}
AQ_Video = {"id": 2, "question": "Video?", "answers": ["Yes", "No", "No", "No"], "indexOfCorrectAnswer": 0,
            "attraction": AttractionVideo}

# Hints
Hint_NotExist = {"id": -1, "attraction": AttractionNotExist, "kind": "HintText", "data": "NotExist"}
Hint_Text = {"id": 0, "attraction": AttractionSimple, "kind": "HintText", "data": "Simple HT"}
Hint_Picture = {"id": 1, "attraction": AttractionSimple, "kind": "HintPicture", "data": "x.jpg"}
Hint_Video = {"id": 2, "attraction": AttractionSimple, "kind": "HintVideo", "data": "x.mp4"}

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


def check(expected, actual, assertFunc, classSerializer=None, many=False):
    jsonActual = actual
    if (actual is not None) and (classSerializer is not None):
        serializerActual = classSerializer(actual, many=many)
        jsonActual = json.loads(json.dumps(serializerActual.data))
    assertFunc(jsonActual, expected)


class Unit_Test_Users(TestCase):
    addUser(UserExist['name'], UserExist['socialNetwork'])

    def test_getUser_NotExist(self):
        check(
            None,
            bl.getUser(UserNotExist),
            self.assertEquals,
            UserSerializer
        )

    def test_getUser_Exist(self):
        check(
            UserExist,
            bl.getUser(UserExist),
            self.assertEquals,
            UserSerializer
        )


class Unit_Test_PreviousUserTrip(TestCase):
    addUser(UserExist['name'], UserExist['socialNetwork'])
    # TODO - continue from here add all data and slice to cases (maybe slice to files which in each file test case and 1 more file of all the data for tests)

    def test_getPreviousUserTrip_NotExist(self):
        check(
            None,
            bl.getPreviousUserTrip(UserNotExist),
            self.assertEquals,
            TripSerializer
        )

    def test_getPreviousUserTrip_Exist(self):
        check(
            Trip_Short,
            bl.getPreviousUserTrip(UserExist),
            self.assertEquals,
            TripSerializer
        )

    def test_getRelevantPreviousTripInformation_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getPreviousUserTrip(UserNotExist)

    def test_getRelevantPreviousTripInformation_New(self):
        check(
            None,
            bl.getRelevantPreviousTripInformation(UserNew),
            self.assertEquals,
            GetRelevantPreviousTripInformationSerializer
        )

    def test_getRelevantPreviousTripInformation_Exist(self):
        check(
            {"groupName": Trip_Short["groupName"], "playersAges": Trip_Short["playersAges"]},
            bl.getRelevantPreviousTripInformation(UserExist),
            self.assertEquals,
            GetRelevantPreviousTripInformationSerializer
        )

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

    def test_createTrip_NotExist(self):
        inp = {"user": UserNotExist, "groupName": "NotExist", "playerAges": [],
               "trackLength": TrackLength.NOT_EXIST.value, "x": next(xGen), "y": next(yGen)}
        self.assertRaises(RuntimeError, bl.createTrip, inp)
        # check(
        #     None,
        #     bl.createTrip(inp),
        #     TripSerializer
        # )

    def test_createTrip_Short(self):
        attraction = Trip_New["attractionsDone"][0]
        user = Trip_New["user"]
        inp = {"user": user, "groupName": Trip_New["groupName"],
               "playerAges": Trip_New["playersAges"], "trackLength": Trip_New["track"]["length"],
               "x": attraction["x"], "y": attraction["y"]}
        actual = bl.createTrip(inp)
        check(
            [Trip_New],
            actual,
            self.assertIn,
            TripSerializer
        )
        check(
            actual,
            bl.getPreviousUserTrip(user),
            self.assertEquals,
            TripSerializer
        )

    def test_createUser_Exist(self):
        with self.assertRaises(RuntimeError):
            bl.createUser(UserExist)

    def test_createUser_NotExist(self):
        check(
            UserNew,
            bl.createUser(UserNew),
            self.assertEquals,
            UserSerializer
        )

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

    def test_getFeedbacks_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getFeedbackInstances(Trip_NotExist)

    def test_getFeedbacks_Exist_No_Feedbacks(self):
        check(
            None,
            bl.getFeedbackInstances(Trip_Short),
            self.assertEquals,
            FeedbackInstanceSerializer,
            True
        )

    def test_getFeedbacks_Exist_With_Feedbacks(self):
        check(
            [FeedbackInstance_Text, FeedbackInstance_Rating],
            bl.getFeedbackInstances(Trip_Empty),
            self.assertCountEqual,
            FeedbackInstanceSerializer,
            True
        )

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

    def test_getAttraction_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getAttraction(AttractionNotExist)

    def test_getAttraction_Exist(self):
        check(
            AttractionSimple,
            bl.getAttraction(AttractionSimple),
            self.assertEquals,
            AttractionSerializer
        )

    def test_getTrip_NotExist(self):
        with self.assertRaises(RuntimeError):
            bl.getTrip(Trip_NotExist)

    def test_getTrip_Exist(self):
        check(
            Trip_Short,
            bl.getTrip(Trip_Short),
            self.assertEquals,
            TripSerializer
        )

    def test_signUp_NotExistedUser(self):
        actual = bl.signUp(UserNew)
        check(
            UserNew,
            actual,
            self.assertEquals,
            UserSerializer
        )
        check(
            None,
            actual["lastSeen"],
            self.assertEquals
        )

    def test_signUp_ExistedUser(self):
        actual = bl.signUp(UserExist)
        check(
            UserExist,
            actual,
            self.assertEquals,
            UserSerializer
        )
        check(
            None,
            actual["lastSeen"],
            self.assertNotEquals
        )
