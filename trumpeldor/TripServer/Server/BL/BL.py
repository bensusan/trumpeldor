from Server.DAL.DAL import DAL_Abstract


# /////////////////////////////////////////////////////////
#                    Functions for BL
# /////////////////////////////////////////////////////////


class BL_Abstract(object):
    DAL = DAL_Abstract()

    class Meta:
        abstract = True

    def getUser(self, user):
        raise NotImplementedError("Should have implemented this")

    def getPreviousUserTrip(self, user):
        raise NotImplementedError("Should have implemented this")

    def getRelevantPreviousTripInformation(self, user):
        raise NotImplementedError("Should have implemented this")

    def getAllAttractionsFromTrack(self, track):
        raise NotImplementedError("Should have implemented this")

    def getClosestAttractionFromTrack(self, track, xUser, yUser):
        raise NotImplementedError("Should have implemented this")

    def getTrackAndNextAttractionByLengthAndUserLocation(self, trackLength, xUser, yUser):
        raise NotImplementedError("Should have implemented this")

    def createTrip(self, data):
        raise NotImplementedError("Should have implemented this")

    def createUser(self, data):
        raise NotImplementedError("Should have implemented this")

    def getHints(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def getFeedbacks(self, trip):
        raise NotImplementedError("Should have implemented this")

    def getAmericanQuestion(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def getAttraction(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def getTrip(self, trip):
        raise NotImplementedError("Should have implemented this")

    def signUp(self, data):
        user = self.getUser(data)
        if user is None:
            user = self.createUser(data)
        return user


class BLProxy(BL_Abstract):
    Implementation = None

    def setImplementation(self, Implementation):
        self.Implementation = Implementation

    def getUser(self, user):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getUser(user)

    def getPreviousUserTrip(self, user):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getPreviousUserTrip(user)

    def getRelevantPreviousTripInformation(self, user):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getRelevantPreviousTripInformation(user)

    def getAllAttractionsFromTrack(self, track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAllAttractionsFromTrack(track)

    def getClosestAttractionFromTrack(self, track, xUser, yUser):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getClosestAttractionFromTrack(track, xUser, yUser)

    def getTrackAndNextAttractionByLengthAndUserLocation(self, trackLength, xUser, yUser):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getTrackAndNextAttractionByLengthAndUserLocation(trackLength, xUser, yUser)

    def createTrip(self, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.createTrip(data)

    def createUser(self, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.createUser(data)

    def getHints(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getHints(attraction)

    def getFeedbacks(self, trip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getFeedbacks(trip)

    def getAmericanQuestion(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAmericanQuestion(attraction)

    def getAttraction(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAttraction(attraction)

    def getTrip(self, trip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getTrip(trip)
