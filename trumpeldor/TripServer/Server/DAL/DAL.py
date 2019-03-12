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

    def getHints(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def getFeedbacks(self):
        raise NotImplementedError("Should have implemented this")

    def getFeedbackInstances(self, trip):
        raise NotImplementedError("Should have implemented this")

    def getAmericanQuestion(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def getAttraction(self, attrId):
        raise NotImplementedError("Should have implemented this")

    def getTrip(self, tripId):
        raise NotImplementedError("Should have implemented this")

    def add_attraction(self, name, x, y, description, picturesURLS, videosURLS):
        raise NotImplementedError("Should have implemented this")

    def add_hint(self, attraction, kind, data):
        raise NotImplementedError("Should have implemented this")

    def add_american_question(self, question, answers, indexOfCorrectAnswer, attraction):
        raise NotImplementedError("Should have implemented this")

    def add_track(self, subTrack, points, length):
        raise NotImplementedError("Should have implemented this")

    def add_feedback_question(self, question, kind):
        raise NotImplementedError("Should have implemented this")

    def get_track(self, track_len):
        raise NotImplementedError("Should have implemented this")

    def get_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def get_attractions(self):
        raise NotImplementedError("Should have implemented this")

    def getAllTracksThatIncludeThisTrack(self, track):
        raise NotImplementedError("Should have implemented this")

    def getOpenMessages(self):
        raise NotImplementedError("Should have implemented this")

    def updateTrip(self, prevTrip, track, groupName, score, playersAges, attractionsDone):
        raise NotImplementedError("Should have implemented this")

    def updateFeedbackInstance(self, feedback, trip, answer):
        raise NotImplementedError("Should have implemented this")

    def createFeedbackInstance(self, feedback, trip):
        raise NotImplementedError("Should have implemented this")

    def getFeedbackById(self, feedbackId):
        raise NotImplementedError("Should have implemented this")

    def updateLastSeenToNow(self, user):
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

    def getHints(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getHints(attraction)

    def getFeedbacks(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getFeedbacks()

    def getFeedbackInstances(self, trip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getFeedbackInstances(trip)

    def getAmericanQuestion(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAmericanQuestion(attraction)

    def getAttraction(self, attrId):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAttraction(attrId)

    def getTrip(self, tripId):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getTrip(tripId)

    def add_attraction(self, name, x, y, description, picturesURLS, videosURLS):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_attraction(name, x, y, description, picturesURLS, videosURLS)

    def add_hint(self, attraction, kind, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_hint(attraction, kind, data)

    def add_american_question(self, question, answers, indexOfCorrectAnswer, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_american_question(question, answers, indexOfCorrectAnswer, attraction)

    def add_track(self, subTrack, points, length):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_track(subTrack, points, length)

    def add_feedback_question(self, question, kind):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_feedback_question(question, kind)

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

    def getAllTracksThatIncludeThisTrack(self, track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAllTracksThatIncludeThisTrack(track)

    def getOpenMessages(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getOpenMessages()

    def updateTrip(self, prevTrip, track, groupName, score, playersAges, attractionsDone):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.updateTrip(prevTrip, track, groupName, score, playersAges, attractionsDone)

    def updateFeedbackInstance(self, feedback, trip, answer):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.updateFeedbackInstance(feedback, trip, answer)

    def createFeedbackInstance(self, feedback, trip):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.createFeedbackInstance(feedback, trip)

    def getFeedbackById(self, feedbackId):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getFeedbackById(feedbackId)

    def updateLastSeenToNow(self, user):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.updateLastSeenToNow(user)
