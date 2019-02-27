from django.test import TestCase
from Server.DAL.DAL import DALProxy
import json
from Server.serializers import AttractionSerializer, TrackSerializer, UserSerializer, AmericanQuestionSerializer, \
    HintSerializer, FeedbackInstanceSerializer, TripSerializer
from Server.DAL.DAL_Implementation import DAL_Implementation
import random
from django.conf import settings
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


class Unit_DAL(TestCase):
    dal = DALProxy()
    dal.setImplementation(DAL_Implementation())

    # Users
    UserNotExist = {"id": -1, "name": "NotExist", "socialNetwork": "Test", "lastSeen": None, "email": None}
    UserExist = {"id": 0, "name": "Exist", "socialNetwork": "Test", "lastSeen": None, "email": None}

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

    def check(self, jsonExpected, actual, classSerializer=None, many=False):
        jsonActual = None
        if actual is not None:
            serializerActual = classSerializer(actual, many=many)
            jsonActual = json.loads(json.dumps(serializerActual.data))
        self.assertEqual(jsonExpected, jsonActual)

    def test_getUser_NotExist(self):
        self.check(
            None,
            self.dal.getUser(self.UserNotExist["name"], self.UserNotExist["socialNetwork"]),
            UserSerializer
        )

    def test_getUser_Exist(self):
        self.check(
            self.UserExist,
            self.dal.getUser(self.UserExist["name"], self.UserExist["socialNetwork"]),
            UserSerializer
        )

    def test_getPreviousTripByUser_NotExist(self):
        self.check(
            None,
            self.dal.getPreviousTripByUser(self.UserNotExist["name"], self.UserNotExist["socialNetwork"]),
            TripSerializer
        )

    def test_getPreviousTripByUser_Exist(self):
        self.check(
            self.Trip_Short,
            self.dal.getPreviousTripByUser(self.UserExist["name"], self.UserExist["socialNetwork"]),
            TripSerializer
        )

    def test_getTrackById_NotExist(self):
        self.check(
            None,
            self.dal.getTrackById(self.TrackNotExist["length"]),
            TrackSerializer
        )

    def test_getTrackById_EmptyTrack(self):
        self.check(
            self.TrackEmpty,
            self.dal.getTrackById(self.TrackEmpty["length"]),
            TrackSerializer
        )

    def test_getTrackById_ShortTrack(self):
        self.check(
            self.TrackShort,
            self.dal.getTrackById(self.TrackShort["id"]),
            TrackSerializer
        )

    def test_getTrackById_MediumTrack(self):
        self.check(
            self.TrackMedium,
            self.dal.getTrackById(self.TrackMedium["id"]),
            TrackSerializer
        )

    def test_getTrackById_LongTrack(self):
        self.check(
            self.TrackLong,
            self.dal.getTrackById(self.TrackLong["id"]),
            TrackSerializer
        )

    def test_getTracksWithSameLength_NotExist(self):
        self.check(
            None,
            self.dal.getTracksWithSameLength(-1),
            TrackSerializer,
            True
        )

    def test_getTracksWithSameLength_Exist(self):
        self.check(
            [self.TrackEmpty, self.TrackShort],
            self.dal.getTracksWithSameLength(1),
            TrackSerializer,
            True
        )

    def test_createTrip_Exist(self):
        self.check(
            None,
            self.dal.createTrip(self.Trip_Short["user"], self.Trip_Short["groupName"], self.Trip_Short["playersAges"],
                                self.Trip_Short["track"],
                                self.Trip_Short["attractionsDone"][len(self.Trip_Short["attractionsDone"])-1]),
            TripSerializer
        )

    def test_createTrip_NotExist(self):
        self.check(
            self.Trip_New,
            self.dal.createTrip(self.Trip_New["user"], self.Trip_New["groupName"], self.Trip_New["playersAges"],
                                self.Trip_New["track"],
                                self.Trip_New["attractionsDone"][len(self.Trip_New["attractionsDone"])-1]),
            TripSerializer
        )

    def test_doneAttractionInTrip(self, trip, attraction):
        expected = self.Trip_AddAttraction.copy()
        self.dal.doneAttractionInTrip(self.Trip_AddAttraction, self.AttractionPicture)
        expected["attractionsDone"] = [self.AttractionPicture] + expected["attractionsDone"]
        self.check(expected, self.Trip_AddAttraction)

    def test_createUser_Validation(self):
        self.check(
            {"name": "Create", "socialNetwork": "Test", "lastSeen": None, "email": None},
            self.dal.createUser("Create", "Test"),
            UserSerializer
        )

    def test_createUser_Verification(self):
        self.assertEqual(self.dal.createUser("Create", "Test"), self.dal.getUser("Create", "Test"))

    def test_getHints_NotExist(self):
        self.check(
            None,
            self.dal.getHints(self.AttractionNotExist),
            HintSerializer,
            True
        )

    def test_getHints_Simple(self):
        self.check(
            [self.Hint_Text, self.Hint_Picture, self.Hint_Video, self.Hint_Map],
            self.dal.getHints(self.AttractionSimple),
            AttractionSerializer
        )

    def test_getFeedbacks_NotExist(self):
        self.check(
            None,
            self.dal.getFeedbacks(self.Trip_NotExist),
            FeedbackInstanceSerializer,
            True
        )

    def test_getFeedbacks_Exist(self):
        self.check(
            [self.FeedbackInstance_Text, self.FeedbackInstance_Rating],
            self.dal.getFeedbacks(self.Trip_Empty),
            FeedbackInstanceSerializer,
            True
        )

    def test_getAmericanQuestion_NotExist(self):
        self.check(
            None,
            self.dal.getAmericanQuestion(self.AQ_NotExist["attraction"]),
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Simple(self):
        self.check(
            self.AQ_Simple,
            self.dal.getAmericanQuestion(self.AQ_Simple["attraction"]),
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Picture(self):
        self.check(
            self.AQ_Picture,
            self.dal.getAmericanQuestion(self.AQ_Picture["attraction"]),
            AmericanQuestionSerializer
        )

    def test_getAmericanQuestion_Video(self):
        self.check(
            self.AQ_Video,
            self.dal.getAmericanQuestion(self.AQ_Video["attraction"]),
            AmericanQuestionSerializer
        )

    def test_getAttraction_NotExist(self):
        self.check(
            None,
            self.dal.getAttraction(self.AttractionNotExist["id"]),
            AttractionSerializer
        )

    def test_getAttraction_Simple(self):
        self.check(
            self.AttractionSimple,
            self.dal.getAttraction(self.AttractionSimple["id"]),
            AttractionSerializer
        )

    def test_getAttraction_Picture(self):
        self.check(
            self.AttractionPicture,
            self.dal.getAttraction(self.AttractionPicture["id"]),
            AttractionSerializer
        )

    def test_getAttraction_Video(self):
        self.check(
            self.AttractionVideo,
            self.dal.getAttraction(self.AttractionVideo["id"]),
            AttractionSerializer
        )

    def test_getTrip_NotExist(self):
        self.check(
            None,
            self.dal.getTrip(self.Trip_NotExist["id"]),
            TripSerializer
        )

    def test_getTrip_Empty(self):
        self.check(
            self.Trip_Empty,
            self.dal.getTrip(self.Trip_Empty["id"]),
            TripSerializer
        )

    def test_getTrip_Short(self):
        self.check(
            self.Trip_Short,
            self.dal.getTrip(self.Trip_Short["id"]),
            TripSerializer
        )