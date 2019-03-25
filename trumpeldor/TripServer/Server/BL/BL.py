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

    def getFeedbackInstances(self, trip):
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

    def getEntertainment(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def add_attraction(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def add_hint(self, attraction, hint):
        raise NotImplementedError("Should have implemented this")

    def add_american_question(self, attraction, a_question):
        raise NotImplementedError("Should have implemented this")

    def add_track(self, track):
        raise NotImplementedError("Should have implemented this")

    def add_feedback_question(self, question, kind):
        raise NotImplementedError("Should have implemented this")

    def get_track(self, track_len):
        raise NotImplementedError("Should have implemented this")

    def get_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def get_attractions(self):
        raise NotImplementedError("Should have implemented this")

    def getExtendedTrack(self, data):
        raise NotImplementedError("Should have implemented this")

    def getOpenMessages(self):
        raise NotImplementedError("Should have implemented this")

    def updateTrip(self, dataTrip):
        raise NotImplementedError("Should have implemented this")

    def getBestScores(self):
        raise NotImplementedError("Should have implemented this")

    def delete_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def edit_attraction(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def delete_american_question(self, id_attraction, id_a_question):
        raise NotImplementedError("Should have implemented this")

    def delete_hint(self, id_attraction, id_hint):
        raise NotImplementedError("Should have implemented this")

    # only editing data of hint, not kind
    def edit_hint(self, id_attraction, hint):
        raise NotImplementedError("Should have implemented this")

    def get_all_tracks(self):
        raise NotImplementedError("Should have implemented this")

    def delete_feedback_question(self, id_feedback):
        raise NotImplementedError("Should have implemented this")

    def get_american_question(self, id_attraction, id_american_question):
        raise NotImplementedError("Should have implemented this")

    def get_hint(self, id_attraction, id_hint):
        raise NotImplementedError("Should have implemented this")

    def get_feedback_question(self, id_feedback):
        raise NotImplementedError("Should have implemented this")




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

    def getFeedbackInstances(self, trip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getFeedbackInstances(trip)

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

    def getEntertainment(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getEntertainment(attraction)

    def add_attraction(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_attraction(attraction)

    def add_hint(self, attraction, hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_hint(attraction, hint)

    def add_american_question(self, attraction, a_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_american_question(attraction, a_question)

    def add_track(self, track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_track(track)

    def add_feedback_question(self, question, kind):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_feedback_question(question)

    def get_track(self, track_len):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_track(track_len)

    def get_attraction(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_attraction(id)

    def get_attractions(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_attractions()

    def getExtendedTrack(self, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getExtendedTrack(data)

    def getOpenMessages(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getOpenMessages()

    def updateTrip(self, dataTrip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.updateTrip(dataTrip)

    def getBestScores(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getBestScores()

    def delete_attraction(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_attraction(id)

    def edit_attraction(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_attraction(attraction)

    def delete_american_question(self, id_attraction, id_a_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_american_question(id_attraction, id_a_question)

    def delete_hint(self, id_attraction, id_hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_hint(id_attraction, id_hint)

    def edit_hint(self, id_attraction, hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_hint(id_attraction, hint)

    def get_all_tracks(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_tracks()

    def delete_feedback_question(self, id_feedback):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_feedback_question(id_feedback)

    def get_american_question(self, id_attraction, id_american_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_american_question(id_attraction, id_american_question)

    def get_hint(self, id_attraction, id_hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_hint(id_attraction, id_hint)

    def get_feedback_question(self, id_feedback):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_feedback_question(id_feedback)
