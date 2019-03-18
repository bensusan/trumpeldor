from math import *
from .BL import BL_Abstract
from Server.DAL.DAL import DALProxy
from Server.serializers import *
from Server.models import *
from itertools import chain
import TripServer.settings as settings

def getDistance(lat1, lon1, lat2, lon2):
    def haversin(x):
        return sin(x / 2) ** 2

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
        return track.points.all() | self.getAllAttractionsFromTrack(track.subTrack)

    def getClosestAttractionFromTrack(self, track, xUser, yUser):
        allAttractions = self.getAllAttractionsFromTrack(track)

        minAttraction, minDist = None, inf
        for attraction in allAttractions:
            dist = getDistance(attraction.x, attraction.y, xUser, yUser)  # Calculate distance
            if minDist > dist:
                minDist = dist
                minAttraction = attraction

        return minAttraction, minDist

    def getMinTrackAndAttraction(self, tracks, xUser, yUser):
        minTrack, minAttraction, minDist = None, None, inf
        for track in tracks:
            attraction, dist = self.getClosestAttractionFromTrack(track, xUser, yUser)
            if minDist > dist:
                minDist, minAttraction, minTrack = dist, attraction, track

        return minTrack, minAttraction

    def getTrackAndNextAttractionByLengthAndUserLocation(self, trackLength, xUser, yUser):
        tracks = self.DAL.getTracksWithSameLength(trackLength)
        return self.getMinTrackAndAttraction(tracks, xUser, yUser)

    def createTrip(self, data):
        track, attraction = self.getTrackAndNextAttractionByLengthAndUserLocation(data['trackLength'], data['x'], data['y'])
        if track is None:
            raise RuntimeError("No tracks in system")
        if attraction is None:
            raise RuntimeError("Tracks are empty")
        user = self.getUser(data['user'])
        user = self.DAL.updateLastSeenToNow(user)
        return self.DAL.createTrip(user, data['groupName'], data['playersAges'], track, attraction)

    def createUser(self, data):
        return self.DAL.createUser(data['name'], data['socialNetwork'])

    def getHints(self, attraction):
        attr = self.getAttraction(attraction)
        return self.DAL.getHints(attr)

    def getFeedbackInstances(self, trip):
        trip = self.getTrip(trip)
        return self.DAL.getFeedbackInstances(trip)

    def getAmericanQuestion(self, attraction):
        attr = self.getAttraction(attraction)
        return self.DAL.getAmericanQuestion(attr)

    def getAttraction(self, attraction):
        return self.DAL.getAttraction(attraction['id'])

    def getTrip(self, trip):
        return self.DAL.getTrip(trip['id'])

    def add_attraction(self, attraction):
        return self.DAL.add_attraction(attraction['name'], attraction['x'], attraction['y'],
                                       attraction['description'], attraction['picturesURLS'], attraction['videosURLS'])

    def add_hint(self, attraction, hint):
        return self.DAL.add_hint(attraction, hint['kind'], attraction['data'])

    def add_american_question(self, attraction, a_question):
        return self.DAL.add_american_question(a_question['question'], a_question['answers'],a_question['indexOfCorrectAnswer'],
                                       a_question['question'], attraction)

    def add_track(self, track):
        return self.DAL.add_track(track['subTrack'], track['points'], track['length'])

    def add_feedback_question(self, question, kind):#question, kind
        return self.DAL.add_feedback_question(question, kind)

    def get_track(self, track_len):
        return self.DAL.add_track(track_len)

    def get_attraction(self, id):
        return self.DAL.get_attraction(id)

    def get_attractions(self):
        return self.DAL.get_attractions()

    def getExtendedTrack(self, data):
        track = self.DAL.getTrackById(data["trackId"])
        tracks = self.DAL.getAllTracksThatIncludeThisTrack(track)
        track, attraction = self.getMinTrackAndAttraction(tracks, data["x"], data["y"])
        return track

    def getOpenMessages(self):
        return self.DAL.getOpenMessages()

    def updateTrip(self, dataTrip):
        trip = self.getTrip(dataTrip)
        trip = self.DAL.updateTrip(
            trip,
            self.DAL.getTrackById(dataTrip["track"]["id"]),
            dataTrip["groupName"],
            dataTrip["score"],
            dataTrip["playersAges"],
            map(lambda x: self.DAL.getAttraction(x["id"]), dataTrip["attractionsDone"]))

        self.DAL.updateLastSeenToNow(self.getUser(dataTrip["user"]))
        self.updateFeedbackInstances(dataTrip["feedbacks"], trip)

    def updateFeedbackInstances(self, feedbackInstancesAsJson, trip):
        for fi in feedbackInstancesAsJson:
            self.DAL.updateFeedbackInstance(self.getFeedback(fi["feedback"]), trip, fi["answer"])

    def getFeedback(self, feedback):
        return self.DAL.getFeedbackById(feedback["id"])

    def getBestScores(self):
        return self.DAL.getAllTrips()[::-1][:settings.TOP_X]

