import math
from .BL import BL_Abstract
from Server.DAL.DAL import DALProxy


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
            return track.points
        return track.points + self.getAllAttractionsFromTrack(track.subTrack)

    def getClosestAttractionFromTrack(self, track, xUser, yUser):
        allAttractions = self.getAllAttractionsFromTrack(track)

        minAttraction, minDist = None, math.inf()
        for attraction in allAttractions:
            dist = math.hypot(attraction['x'] - xUser, attraction['y'] - yUser)  # Calculate distance
            if minDist > dist:
                minDist = dist
                minAttraction = attraction

        return minAttraction, minDist

    def getTrackAndNextAttractionByLengthAndUserLocation(self, trackLength, xUser, yUser):
        tracks = self.DAL.getTracksWithSameLength(trackLength)

        minTrack, minAttraction, minDist = None, None, math.inf()
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
        trip = self.DAL.createTrip(data['user'], data['groupName'], data['playersAges'], track, attraction)
        return trip

    def createUser(self, data):
        return self.DAL.createUser(data['name'], data['socialNetwork'])

# def getUser(user):
#     return DAL.getUser(user['name'], user['socialNetwork'])


# def getPreviousUserTrip(user):
#     return DAL.getPreviousTripByUser(user['name'], user['socialNetwork'])


# def getRelevantPreviousTripInformation(user):
#     trip = getPreviousUserTrip(user)
#     if trip is not None:
#         return {'groupName': trip.groupName, 'playersAges': trip.playersAges}
#     return trip


# def getAllAttractionsIdsFromTrack(track):
#     attractionsIds = []
#     while track is not None:
#         attractionsIds += track['points']
#         track = DAL.getTrackById(track['subTrack'])
#     return attractionsIds


# def getClosestAttractionIdFromTrack(track, xUser, yUser):
#     allAttractionsIds = getAllAttractionsIdsFromTrack(track)
#     minAttractionId, minDist = -1, math.inf()
#
#     for attractionId in allAttractionsIds:
#         attraction = DAL.getAttractionById(attractionId)
#         dist = math.hypot(attraction['x'] - xUser, attractionId['y'] - yUser)   # Calculate distance
#         if minDist > dist:
#             minDist = dist
#             minAttractionId = attractionId
#     return minAttractionId, minDist


# def getTrackAndNextAttractionByLengthAndUserLocation(trackLength, xUser, yUser):
#     tracks = DAL.getTracksWithSameLength(trackLength)
#
#     minTrack = None
#     minAttractionId = None
#     minDist = math.inf()
#     for track in tracks:
#         attractionId, dist = getClosestAttractionIdFromTrack(track, xUser, yUser)
#         if minDist > dist:
#             minDist = dist
#             minAttractionId = attractionId
#             minTrack = track
#     if minAttractionId is None:
#         raise RuntimeError
#     return minTrack, minAttractionId


# def createTrip(data):
#     track, attractionId = getTrackAndNextAttractionByLengthAndUserLocation(data['trackLength'], data['x'], data['y'])
#     attraction = DAL.getAttractionById(attractionId)
#     return DAL.createTrip(data['user'], data['groupName'], data['playersAges'], track, attraction)
