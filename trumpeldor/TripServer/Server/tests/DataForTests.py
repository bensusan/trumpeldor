import random
from enum import Enum
from Server.Services import *
from Server.models import Hint, Feedback


class TrackLength(Enum):
    NOT_EXIST = -1
    EMPTY = 1
    SHORT = 1
    MEDIUM = 2
    LONG = 3


def randomValidNumber(Min, Max):
    while True:
        yield random.random() * Max + Min


Settings = \
    {
        "boundaries":
            [
                0,
                0,
                0,
                0
            ],
        "logo": addPrefixUrlToSpecificName("test.jpg"),
        "loginHours": 36,
        'scoreRules':
            [
                {'ruleName': 'hmtt', 'score': -10},
                {'ruleName': 'aqm', 'score': -2},
                {'ruleName': 'aqc', 'score': 10},
                {'ruleName': 'aa', 'score': 50},
                {'ruleName': 'sps', 'score': 10},
                {'ruleName': 'ttd', 'score': 10},
                {'ruleName': 'ps', 'score': 10}
            ]
    }


# Users
UserNotExist = \
    {
        "name": "NotExist",
        "socialNetwork": "Test",
        "lastSeen": None,
        "email": None
    }
UserExist = \
    {
        "name": "Exist",
        "socialNetwork": "Test",
        "lastSeen": None,
        "email": None
    }
UserNew = \
    {
        "name": "New",
        "socialNetwork": "Test",
        "lastSeen": None,
        "email": None
    }

# Attractions
xGen = randomValidNumber(Settings["boundaries"][0], Settings["boundaries"][1])
yGen = randomValidNumber(Settings["boundaries"][2], Settings["boundaries"][3])
AttractionNotExist = \
    {
        "name": "NotExist",
        "x": next(xGen),
        "y": next(yGen),
        "description": "",
        "picturesURLS":
            [],
        "videosURLS":
            []
    }
AttractionSimple = \
    {
        "name": "Simple",
        "x": next(xGen),
        "y": next(yGen),
        "description": "",
        "picturesURLS":
            [],
        "videosURLS":
            []
    }
AttractionPicture = \
    {
        "name": "Simple",
        "x": next(xGen),
        "y": next(yGen),
        "description": "",
        "picturesURLS":
            addPrefixUrl(
                [
                    "test.jpg"
                ]),
        "videosURLS":
            []
    }
AttractionVideo = \
    {
        "name": "Simple",
        "x": next(xGen),
        "y": next(yGen),
        "description": "",
        "picturesURLS": [],
        "videosURLS": addPrefixUrl(
            [
                "test.mp4"
            ])
    }

# Tracks

TrackNotExist = \
    {
        "subTrack": None,
        "points":
            [],
        "length": TrackLength.NOT_EXIST.value
    }
TrackEmpty = \
    {
        "subTrack": None,
        "points":
            [],
        "length": TrackLength.EMPTY.value
    }
TrackShort = \
    {
        "subTrack": None,
        "points":
            [
                AttractionSimple
            ],
        "length": TrackLength.SHORT.value
    }
TrackMedium = \
    {
        "subTrack": TrackShort,
        "points":
            [
                AttractionPicture
            ],
        "length": TrackLength.MEDIUM.value
    }
TrackLong = \
    {
        "subTrack": TrackMedium,
        "points":
            [
                AttractionVideo
            ],
        "length": TrackLength.LONG.value
    }

# AmericanQuestions
AQ_NotExist = \
    {
        "question": "NotExist?",
        "answers":
            [
                "Yes"
            ],
        "indexOfCorrectAnswer":
            [
                0
            ],
        "attraction": AttractionNotExist
    }
AQ_Simple = \
    {
        "question": "Simple?",
        "answers":
            [
                "Yes",
                "No"
            ],
        "indexOfCorrectAnswer":
            [
                0
            ],
        "attraction": AttractionSimple
    }
AQ_Picture = \
    {
        "question": "Picture?",
        "answers":
            [
                "Yes",
                "No",
                "No"
            ],
        "indexOfCorrectAnswer":
            [
                0
            ],
        "attraction": AttractionPicture
    }
AQ_Video = \
    {
        "question": "Video?",
        "answers":
            [
                "Yes",
                "No",
                "No",
                "No"
            ],
        "indexOfCorrectAnswer":
            [
                0
            ],
        "attraction": AttractionVideo
    }

# SlidingPuzzle
SP_NotExist = \
    {
        "attraction": AttractionNotExist,
        "description": "SP_NotExist",
        "piecesURLS": addPrefixUrl(
            [
                "example00.jpeg",
                "example01.jpeg",
                "example02.jpeg",
                "example10.jpeg",
                "example11.jpeg",
                "example12.jpeg",
                "example20.jpeg",
                "example21.jpeg",
                "example22.jpeg"
            ]),
        "width": 3,
        "height": 3
    }

SP_Simple = \
    {
        "attraction": AttractionSimple,
        "description": "SP_Simple",
        "piecesURLS": addPrefixUrl(
            [
                "example00.jpeg",
                "example01.jpeg",
                "example02.jpeg",
                "example10.jpeg",
                "example11.jpeg",
                "example12.jpeg",
                "example20.jpeg",
                "example21.jpeg",
                "example22.jpeg"
            ]),
        "width": 3,
        "height": 3
    }

# Puzzle
Puzzle_NotExist = \
    {
        "attraction": AttractionNotExist,
        "description": "Puzzle_NotExist",
        "piecesURLS": addPrefixUrl(
            [
                "example00.jpeg",
                "example01.jpeg",
                "example02.jpeg",
                "example10.jpeg",
                "example11.jpeg",
                "example12.jpeg",
                "example20.jpeg",
                "example21.jpeg",
                "example22.jpeg"
            ]),
        "width": 3,
        "height": 3
    }

Puzzle_Picture = \
    {
        "attraction": AttractionPicture,
        "description": "Puzzle_Simple",
        "piecesURLS": addPrefixUrl(
            [
                "example00.jpeg",
                "example01.jpeg",
                "example02.jpeg",
                "example10.jpeg",
                "example11.jpeg",
                "example12.jpeg",
                "example20.jpeg",
                "example21.jpeg",
                "example22.jpeg"
            ]),
        "width": 3,
        "height": 3
    }

# Taking Picture
TP_NotExist = \
    {
        "attraction": AttractionNotExist,
        "description": "TP_NotExist"
    }

TP_Video = \
    {
        "attraction": AttractionVideo,
        "description": "TP_Video"
    }


# Hints
Hint_NotExist = \
    {
        "attraction": AttractionNotExist,
        "kind": "NotExist",
        "data": "NotExist"
    }
Hint_Text = \
    {
        "attraction": AttractionSimple,
        "kind": Hint.HINT_TEXT,
        "data": "Simple HT"
    }
Hint_Picture = \
    {
        "attraction": AttractionSimple,
        "kind": Hint.HINT_PICTURE,
        "data": addPrefixUrlToSpecificName("test.jpg")
    }
Hint_Video = \
    {
        "attraction": AttractionSimple,
        "kind": Hint.HINT_VIDEO,
        "data": addPrefixUrlToSpecificName("test.mp4")
    }

# Feedbacks
Feedback_NotExist = \
    {
        "question": "NotExist?",
        "kind": "NotExist"
    }
Feedback_Text = \
    {
        "question": "Text?",
        "kind": Feedback.FEEDBACK_TEXT
    }
Feedback_Rating = \
    {
        "question": "Rating?",
        "kind": Feedback.FEEDBACK_RATING
    }

# Trip
Trip_NotExist = \
    {
        "user": UserNotExist,
        "groupName": "NotExist",
        "playersAges":
            [],
        "score": 0,
        "track": TrackNotExist,
        "attractionsDone":
            []
    }
Trip_Empty = \
    {
        "user": UserExist,
        "groupName": "ExistEmpty",
        "playersAges":
            [
                10,
                11
            ],
        "score": 0,
        "track": TrackEmpty,
        "attractionsDone":
            []
    }
Trip_Short = \
    {
        "user": UserExist,
        "groupName": "ExistShort",
        "playersAges":
            [
                10,
                11
            ],
        "score": 300,
        "track": TrackShort,
        "attractionsDone":
            [
                AttractionSimple
            ]
    }
Trip_New = \
    {
        "user": UserExist,
        "groupName": "New",
        "playersAges":
            [
                1,
                2
            ],
        "score": 0,
        "track": TrackShort,
        "attractionsDone":
            [
                AttractionSimple
            ]
    }
Trip_AddAttraction = \
    {
        "user": UserExist,
        "groupName": "Add attraction",
        "playersAges":
            [
                10
            ],
        "score": 200,
        "track": TrackMedium,
        "attractionsDone":
            [
                AttractionSimple
            ]
    }

# Feedbacks Instances
FeedbackInstance_NotExist = \
    {
        "feedback": Feedback_NotExist,
        "trip": Trip_NotExist,
        "answer": "NotExist"
    }
FeedbackInstance_Text = \
    {
        "feedback": Feedback_Text,
        "trip": Trip_Empty,
        "answer": "Empty and Text"
    }
FeedbackInstance_Rating = \
    {
        "feedback": Feedback_Rating,
        "trip": Trip_Empty,
        "answer": "3"
    }
