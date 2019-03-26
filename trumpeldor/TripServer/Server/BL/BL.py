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

    def add_attraction(self, attraction):
        raise NotImplementedError("Should have implemented this")

    def add_hint(self, id_attraction, hint):
        raise NotImplementedError("Should have implemented this")

    def add_american_question(self, id_attraction, a_question):
        raise NotImplementedError("Should have implemented this")

    def add_track(self, track):
        raise NotImplementedError("Should have implemented this")

    def add_feedback_question(self, question, kind):
        raise NotImplementedError("Should have implemented this")

    def get_track(self, id):
        raise NotImplementedError("Should have implemented this")

    def get_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def get_attractions(self):
        raise NotImplementedError("Should have implemented this")

    def getExtendedTrack(self, data):
        raise NotImplementedError("Should have implemented this")

    def delete_attraction(self, id):
        raise NotImplementedError("Should have implemented this")

    def edit_attraction(self, id, attraction):
        raise NotImplementedError("Should have implemented this")

    def delete_american_question(self, id_attraction, id_a_question):
        raise NotImplementedError("Should have implemented this")

    def delete_hint(self, id_attraction, id_hint):
        raise NotImplementedError("Should have implemented this")

    # only editing data of hint, not kind
    def edit_hint(self, id_attraction, id_hint_to_edit, hint):
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

    def add_attraction_to_track(self, id_track, x, y):
        raise NotImplementedError("Should have implemented this")

    def delete_attraction_from_track(self, id_track, x ,y):
        raise NotImplementedError("Should have implemented this")

    def delete_track(self, id_track):
        raise NotImplementedError("Should have implemented this")

    def get_track_by_length(self, len):
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

    def add_attraction(self, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_attraction(attraction)

    def add_hint(self, id_attraction, hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_hint(id_attraction, hint)

    def add_american_question(self, id_attraction, a_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_american_question(id_attraction, a_question)

    def add_track(self, track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_track(track)

    def add_feedback_question(self, question, kind):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_feedback_question(question)

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

    def getExtendedTrack(self, data):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.getExtendedTrack(data)

    def delete_attraction(self, id):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_attraction(id)

    def edit_attraction(self, id, attraction):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_attraction(id, attraction)

    def delete_american_question(self, id_attraction, id_a_question):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_american_question(id_attraction, id_a_question)

    def delete_hint(self, id_attraction, id_hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_hint(id_attraction, id_hint)

    def edit_hint(self, id_attraction, id_hint_to_edit, hint):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.edit_hint(id_attraction, id_hint_to_edit, hint)

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

    def add_attraction_to_track(self, id_track, x, y):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.add_attraction_to_track(id_track, x, y)

    def delete_attraction_from_track(self, id_track, x, y):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_attraction_from_track(id_track, x, y)

    def delete_track(self, id_track):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.delete_track(id_track)

    def get_track_by_length(self, len):
        if self.Implementation is None:
            raise NotImplementedError("Should have implemented this")
        return self.Implementation.get_track_by_length(len)