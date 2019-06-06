from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
import math
from Server.serializers import *
import json


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


def isJson(obj):
    try:
        json.loads(obj)
        return True
    except ValueError as error:
        return False


def assertInForTests(actual, listContainsExpected, assertTrue):
    for expected in listContainsExpected:
        if assertEqualsForTests(actual, expected):
            return True
    return False


# Necessary to get self.assertEquals
def assertEqualsForTests(actual, expected, assertEquals=None):
    answer = True
    answer &= isJson(expected) != isJson(actual)
    if assertEquals is not None:
        assertEquals(isJson(expected), isJson(actual))
    answer &= isinstance(expected, list) != isinstance(actual, list)
    if assertEquals is not None:
        assertEquals(isinstance(expected, list), isinstance(actual, list))
    if isJson(actual):
        for keyE, valueE in expected.items():
            for keyA, valueA in actual.items():
                if keyE == keyE:
                    answer &= assertEqualsForTests(valueE, valueA, assertEquals)
    elif isinstance(actual, list):
        assertEquals(len(actual), len(list))
        for e, a in zip(expected, actual):
            answer &= assertEqualsForTests(e, a, assertEquals)

    else:
        answer &= expected == actual
        if assertEquals is not None:
            assertEquals(expected, actual)
    return answer


def check(expected, actual, assertFunc, classSerializer=None, many=False):
    jsonActual = actual
    if (actual is not None) and (classSerializer is not None):
        serializerActual = classSerializer(actual, many=many)
        jsonActual = json.loads(json.dumps(serializerActual.data))
    assertFunc(jsonActual, expected)
