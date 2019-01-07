from Server.models import *
from .DAL import DAL_Abstract


class DAL_Implementation(DAL_Abstract):

    def getUser(self, name, socialNetwork):
        return User.objects.filter(name=name, socialNetwork=socialNetwork).first()

    def getPreviousTripByUser(self, name, socialNetwork):
        return Trip.objects.filter(user=self.getUser(name, socialNetwork)).last()

    def getTrackById(self, trackId):
        return Track.objects.filter(id=trackId)

    def getTracksWithSameLength(self, trackLength):
        return Track.objects.filter(length=trackLength)

    def createTrip(self, user, groupName, playersAges, track, attraction):
        trip = Trip(user=user, groupName=groupName, playersAges=playersAges, track=track)
        trip.save()
        self.doneAttractionInTrip(trip, attraction)
        return trip

    def doneAttractionInTrip(self, trip, newAttraction):
        trip.attractionsDone.add(newAttraction)

    def createUser(self, name, socialNetwork):
        user = User(name=name, socialNetwork=socialNetwork)
        user.save()
        return user


# def getUser(name, socialNetwork):
#     return User.objects.filter(name=name, socialNetwork=socialNetwork).first()


# def getPreviousTripByUser(name, socialNetwork):
#     return Trip.objects.filter(user=getUser(name, socialNetwork)).last()


# def getAttractionById(attractionId):
#     return Attraction.objects.filter(id=attractionId)


# def getTrackById(trackId):
#     return Track.objects.filter(id=trackId)


# def getTracksWithSameLength(trackLength):
#     return Track.objects.filter(length=trackLength)


# def createTrip(user, groupName, playersAges, track, attraction):
#     trip = Trip(user=user, groupName=groupName, playersAges=playersAges, track=track, nextAttraction=attraction)
#     trip.save()
#     return trip
