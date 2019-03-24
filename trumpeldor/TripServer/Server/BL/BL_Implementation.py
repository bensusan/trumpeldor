from math import *
from .BL import BL_Abstract
from Server.DAL.DAL import DALProxy
from Server.serializers import *
from Server.models import *
from itertools import chain


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
        return self.DAL.createTrip(user, data['groupName'], data['playersAges'], track, attraction)

    def createUser(self, data):
        return self.DAL.createUser(data['name'], data['socialNetwork'])

    def getHints(self, attraction):
        attr = self.getAttraction(attraction)
        return self.DAL.getHints(attr)

    def getFeedbacks(self, trip):
        trip = self.getTrip(trip)
        return self.DAL.getFeedbacks(trip)

    def getAmericanQuestion(self, id_attraction):
        attr = self.get_attraction(id_attraction)
        return self.DAL.getAmericanQuestion(attr)

    def getAttraction(self, attraction):
        return self.DAL.getAttraction(attraction['id'])

    def getTrip(self, trip):
        return self.DAL.getTrip(trip['id'])

    def add_attraction(self, attraction):
        if self.get_attraction_by_x_y(attraction['x'], attraction['y']) is None:
            return self.DAL.add_attraction(attraction['name'], attraction['x'], attraction['y'],
                                       attraction['description'], attraction['picturesURLS'], attraction['videosURLS'])

    def add_hint(self, id_attraction, hint):
        return self.DAL.add_hint(id_attraction, hint['kind'], hint['data'])

    def add_american_question(self, id_attraction, a_question):
        return self.DAL.add_american_question(id_attraction, a_question['question'], a_question['answers'],
                                              a_question['indexOfCorrectAnswer'])

    def add_track(self, track):
        return self.DAL.add_track(track['points'], track['length'])

    def add_feedback_question(self, question, kind):#question, kind
        return self.DAL.add_feedback_question(question, kind)

    def get_track(self, track_len):
        return self.DAL.get_track(track_len)

    def get_attraction(self, id):
        return self.DAL.get_attraction(id)

    def get_attractions(self):
        return self.DAL.get_attractions()

    def getExtendedTrack(self, data):
        track = self.DAL.getTrackById(data["track"]["id"])
        tracks = self.DAL.getAllTracksThatIncludeThisTrack(track)
        track, attraction = self.getMinTrackAndAttraction(tracks, data["x"], data["y"])
        return track

    def delete_attraction(self, id):
        if self.get_attraction(id) is not None:
            return self.DAL.delete_attraction(id)

    def edit_attraction(self, id, attraction):
        if self.get_attraction(id) is not None:
            return self.DAL.edit_attraction(id, attraction['name'], attraction['x'], attraction['y'],
                                            attraction['description'], attraction['picturesURLS'], attraction['videosURLS'])

    def delete_american_question(self, id_attraction, id_a_question):
        if self.get_american_question(id_attraction, id_a_question):
            return self.DAL.delete_american_question(id_attraction, id_a_question)

    def delete_hint(self, id_attraction, id_hint):
        if self.get_hint(id_attraction, id_hint):
            return self.DAL.delete_hint(id_attraction, id_hint)

    def edit_hint(self, id_attraction, id_hint_to_edit, hint):
        hint_before_edit = self.get_hint(id_attraction, id_hint_to_edit)
        if hint_before_edit is not None and hint_before_edit.kind == hint['kind']:
            return self.DAL.edit_hint(id_attraction, id_hint_to_edit, hint['data'])

    def get_all_tracks(self):
        return self.DAL.get_all_tracks()

    def delete_feedback_question(self, id_feedback):
        if self.get_feedback_question(id_feedback) is not None:
            return self.DAL.delete_feedback_question(id_feedback)

    def get_american_question(self, id_attraction, id_american_question):
        if self.get_attraction(id_attraction) is not None:
            return self.DAL.get_american_question(id_attraction, id_american_question)

    def get_hint(self, id_attraction, id_hint):
        if self.get_attraction(id_attraction) is not None:
            return self.DAL.get_hint(id_attraction, id_hint)

    def get_feedback_question(self, id_feedback):
        return self.DAL.get_feedback_question(id_feedback)

    def get_attraction_by_x_y(self, x, y):
        return self.DAL.get_attraction_by_x_y(x, y)

    def get_all_aquestions_for_attraction(self, id_attraction):
        return self.DAL.get_all_aquestions_for_attraction(id_attraction)

    def get_all_hints_for_attraction(self, id_attraction):
        return self.DAL.get_all_hints_for_attraction(id_attraction)
