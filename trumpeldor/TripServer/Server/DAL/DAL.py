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

    def add_hint(self, id_attraction, kind, data, description):
        raise NotImplementedError("Should have implemented this")

    def add_american_question(self, id_attraction, question, answers, indexOfCorrectAnswer):
        raise NotImplementedError("Should have implemented this")

    def add_track(self, subTrack, points, length):
        raise NotImplementedError("Should have implemented this")

    def add_feedback_question(self, question, kind):
        raise NotImplementedError("Should have implemented this")

    def get_track(self, id):
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

    def getAllTrips(self):
        raise NotImplementedError("Should have implemented this")

    def getSlidingPuzzle(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def delete_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def edit_attraction(self, id, name, x, y, description, picturesURLS, videosURLS):
        raise NotImplementedError("Should have implemented this")

    def delete_american_question(self, id_attraction, id_a_question):
        raise NotImplementedError("Should have implemented this")

    def delete_hint(self, id_attraction, id_hint, data):
        raise NotImplementedError("Should have implemented this")

    def edit_hint(self, id_attraction, id_hint, data):
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

    def get_attraction_by_x_y(self, x, y):
        raise NotImplementedError("Should have implemented this")

    def get_all_aquestions_for_attraction(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def get_all_hints_for_attraction(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def add_attraction_to_track(self, id_track, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def delete_attraction_from_track(self, id_track,id_attraction):
        raise NotImplementedError("Should have implemented this")

    def delete_track(self, id_track):
        raise NotImplementedError("Should have implemented this")

    def get_track_by_length(self, len):
        raise NotImplementedError("Should have implemented this")

    def edit_track(self, id_track, points):
        raise NotImplementedError("Should have implemented this")

    def get_all_feedback_questions(self):
        raise NotImplementedError("Should have implemented this")

    def add_info(self, info):
        raise NotImplementedError("Should have implemented this")

    def get_info(self):
        raise NotImplementedError("Should have implemented this")

    def delete_info(self, id):
        raise NotImplementedError("Should have implemented this")

    def get_all_sliding_puzzles_for_attraction(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def add_sliding_puzzle(self, id_attraction, piecesURLS, width, height, description):
        raise NotImplementedError("Should have implemented this")

    def delete_sliding_puzzle(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def get_all_puzzles_for_attraction(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def add_puzzle(self, id_attraction, pictureURL, width, height, description):
        raise NotImplementedError("Should have implemented this")

    def delete_puzzle(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def get_all_find_the_differences_for_attraction(self, id_attraction):
        raise NotImplementedError("Should have implemented this")

    def add_find_the_differences(self, id_attraction, pictureURL, differences, description):
        raise NotImplementedError("Should have implemented this")

    def delete_find_the_differences(self, id_attraction):
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

    def add_hint(self, id_attraction, kind, data, description):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_hint(id_attraction, kind, data, description)

    def add_american_question(self, id_attraction, question, answers, indexOfCorrectAnswer):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_american_question(id_attraction, question, answers, indexOfCorrectAnswer)

    def add_track(self, subTrack, points, length):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_track(subTrack, points, length)

    def add_feedback_question(self, question, kind):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_feedback_question(question, kind)

    def get_track(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_track(id)

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

    def getAllTrips(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getAllTrips()

    def getSlidingPuzzle(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getSlidingPuzzle(attraction)

    def delete_attraction(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_attraction(id)

    def edit_attraction(self, id, name, x, y, description, picturesURLS, videosURLS):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_attraction(id, name, x, y, description, picturesURLS, videosURLS)

    def delete_american_question(self, id_attraction, id_a_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_american_question(id_attraction, id_a_question)

    def delete_hint(self, id_attraction, id_hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_hint(id_attraction, id_hint)

    def edit_hint(self, id_attraction, id_hint, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_hint(id_attraction, id_hint, data)

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

    def get_attraction_by_x_y(self, x, y):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_attraction_by_x_y(x, y)

    def get_all_aquestions_for_attraction(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_aquestions_for_attraction(id_attraction)

    def get_all_hints_for_attraction(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_hints_for_attraction(id_attraction)

    def add_attraction_to_track(self, id_track, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_attraction_to_track(id_track, id_attraction)

    def delete_attraction_from_track(self, id_track, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_attraction_from_track(id_track, id_attraction)

    def delete_track(self, id_track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_track(id_track)

    def get_track_by_length(self, len):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_track_by_length(len)

    def edit_track(self, id_track, points):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_track(id_track, points)

    def get_all_feedback_questions(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_feedback_questions()

    def add_info(self, info):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_info(info)

    def get_info(self):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_info()

    def delete_info(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_info(id)

    def get_all_sliding_puzzles_for_attraction(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_sliding_puzzles_for_attraction(id_attraction)

    def add_sliding_puzzle(self, id_attraction, piecesURLS, width, height, description):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_sliding_puzzle(id_attraction, piecesURLS, width, height, description)

    def delete_sliding_puzzle(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_sliding_puzzle(id_attraction)

    def get_all_puzzles_for_attraction(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_puzzles_for_attraction(id_attraction)

    def add_puzzle(self, id_attraction, pictureURL, width, height, description):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_puzzle(id_attraction, pictureURL, width, height, description)

    def delete_puzzle(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_puzzle(id_attraction)

    def get_all_find_the_differences_for_attraction(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_all_find_the_differences_for_attraction(id_attraction)

    def add_find_the_differences(self, id_attraction, pictureURL, differences, description):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_find_the_differences(id_attraction, pictureURL, differences, description)

    def delete_find_the_differences(self, id_attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_find_the_differences(id_attraction)
