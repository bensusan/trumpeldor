from django.test import TestCase
from Server.DAL.DAL import *
import json
from Server.serializers import *
from Server.DAL.DAL_Implementation import DAL_Implementation


# Need to copy DB and to work on the DB's copy...
class MyTestCase(TestCase):
    dal = DALProxy()
    dal.setImplementation(DAL_Implementation())

    def check(self, jsonExpected, actual, classSerializer=None, many=False):
        jsonActual = None
        if actual is not None:
            serializerActual = classSerializer(actual, many=many)
            jsonActual = json.loads(json.dumps(serializerActual.data))
        self.assertEqual(jsonExpected, jsonActual)

    def test_getUser_notExist(self):
        self.check(None, self.dal.getUser("NotExist", "Test"), UserSerializer)

    def test_getUser_Exist(self):
        actual = self.dal.getUser("Exist", "Test")
        expected = None
        self.check( {"name": "Exist", "socialNetwork": "Test", "lastSeen": None, "email": None},
                    self.dal.getUser("Exist", "Test"),
                    UserSerializer)

    def test_getPreviousTripByUser(self, name, socialNetwork):
        raise NotImplementedError("Should have implemented this")

    def test_getTrackById(self, trackId):
        raise NotImplementedError("Should have implemented this")

    def test_getTracksWithSameLength(self, trackLength):
        raise NotImplementedError("Should have implemented this")

    def test_createTrip(self, user, groupName, playersAges, track, attraction):
        raise NotImplementedError("Should have implemented this")

    def test_doneAttractionInTrip(self, trip, attraction):
        raise NotImplementedError("Should have implemented this")

    def test_createUser(self, name, socialNetwork):
        raise NotImplementedError("Should have implemented this")

    def test_getHints(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def test_getFeedbacks(self, trip):
        raise NotImplementedError("Should have implemented this")

    def test_getAmericanQuestion(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def test_getAttraction(self, attrId):
        raise NotImplementedError("Should have implemented this")

    def test_getTrip(self, tripId):
        raise NotImplementedError("Should have implemented this")
