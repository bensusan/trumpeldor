from math import *
from .BL import BL_Abstract
from Server.DAL.DAL import DALProxy
from Server.serializers import *
from Server.models import *


def getDistance(lat1, lon1, lat2, lon2):
    def haversin(x):
        return sin(x /  2) ** 2

    return 2 * asin(sqrt(
        haversin(lat2 - lat1) +
        cos(lat1) * cos(lat2) * haversin(lon2 - lon1)))


class BL_Implementation(BL_Abstract):

    def __init__(self):
        self.DAL = DALProxy()

    def setDAL(self, DAL_Impl):
        self.DAL.setImplementation(DAL_Impl)

    def getUser(self, user):
        return self.DAL.getUser(user['name'], user['socialNetwork'])

    def getPreviousUserTrip(self, dataUser):
        return self.DAL.getPreviousTripByUser(dataUser['name'], dataUser['socialNetwork'])

    def getRelevantPreviousTripInformation(self, dataUser):
        trip = self.getPreviousUserTrip(dataUser)
        ans = {'groupName': '', 'playersAges': []}
        if trip is not None:
            ans['groupName'] = trip.groupName
            ans['playersAges'] = trip.playersAges
        return ans

    def getAllAttractionsFromTrack(self, track):
        if track.subTrack is None:
            return track.points.all()
        return track.points.all() + self.getAllAttractionsFromTrack(track.subTrack)

    def getClosestAttractionFromTrack(self, track, xUser, yUser):
        allAttractions = self.getAllAttractionsFromTrack(track)

        minAttraction, minDist = None, inf
        for attraction in allAttractions:
            dist = getDistance(attraction.x, attraction.y, xUser, yUser)  # Calculate distance
            if minDist > dist:
                minDist = dist
                minAttraction = attraction

        return minAttraction, minDist

    def getTrackAndNextAttractionByLengthAndUserLocation(self, trackLength, xUser, yUser):
        tracks = self.DAL.getTracksWithSameLength(trackLength)

        minTrack, minAttraction, minDist = None, None, inf
        for track in tracks:
            attraction, dist = self.getClosestAttractionFromTrack(track, xUser, yUser)
            if minDist > dist:
                minDist, minAttraction, minTrack = dist, attraction, track

        return minTrack, minAttraction

    def createTrip(self, data):
        track, attraction = self.getTrackAndNextAttractionByLengthAndUserLocation(data['trackLength'], data['x'], data['y'])
        if track is None:
            raise RuntimeError("No tracks in system")
        if attraction is None:
            raise RuntimeError("Tracks are empty")
        user = self.getUser(data['user'])
        return self.DAL.createTrip(user, data['groupName'], data['playersAges'], track, attraction)

    def createUser(self, data):
        return self.DAL.createUser(data['name'], data['socialNetwork'])

    def getHints(self, attraction):
        attr = self.getAttraction(attraction)
        return self.DAL.getHints(attr)

    def getFeedbacks(self, trip):
        trip = self.getTrip(trip)
        return self.DAL.getFeedbacks(trip)

    def getAmericanQuestion(self, attraction):
        attr = self.getAttraction(attraction)
        return self.DAL.getAmericanQuestion(attr)

    def getAttraction(self, attraction):
        return self.DAL.getAttraction(attraction['id'])

    def getTrip(self, trip):
        return self.DAL.getTrip(trip['id'])