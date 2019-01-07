class DAL_Abstract(object):
    class Meta:
        abstract = True

    def getUser(self, name, socialNetwork):
        raise NotImplementedError("Should have implemented this")

    def getPreviousTripByUser(self, name, socialNetwork):
        raise NotImplementedError("Should have implemented this")

    def getTrackById(self, trackId):
        raise NotImplementedError("Should have implemented this")

    def getTracksWithSameLength(self, trackLength):
        raise NotImplementedError("Should have implemented this")

    def createTrip(self, user, groupName, playersAges, track, attraction):
        raise NotImplementedError("Should have implemented this")

    def doneAttractionInTrip(self, trip, attraction):
        raise NotImplementedError("Should have implemented this")

    def createUser(self, name, socialNetwork):
        raise NotImplementedError("Should have implemented this")


class DALProxy(DAL_Abstract):
    Implementation = None

    def setImplementation(self, Implementation):
        self.Implementation = Implementation

    def getUser(self, name, socialNetwork):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getUser(name, socialNetwork)

    def getPreviousTripByUser(self, name, socialNetwork):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getPreviousTripByUser(name, socialNetwork)

    def getTrackById(self, trackId):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getTrackById(trackId)

    def getTracksWithSameLength(self, trackLength):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getTracksWithSameLength(trackLength)

    def createTrip(self, user, groupName, playersAges, track, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.createTrip(user, groupName, playersAges, track, attraction)

    def doneAttractionInTrip(self, trip, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.doneAttractionInTrip(trip, attraction)

    def createUser(self, name, socialNetwork):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.createUser(name, socialNetwork)
