import null

from Server.models import *
from .DAL import DAL_Abstract


class DAL_Implementation(DAL_Abstract):

    def getUser(self, name, socialNetwork):
        return User.objects.filter(name=name, socialNetwork=socialNetwork).first()

    def getPreviousTripByUser(self, name, socialNetwork):
        return Trip.objects.filter(user=self.getUser(name, socialNetwork)).last()

    def getTrackById(self, trackId):
        return Track.objects.filter(id=trackId).first()

    def getTracksWithSameLength(self, trackLength):
        return Track.objects.filter(length=trackLength).all()

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

    def getHints(self, attraction):
        return Hint.objects.filter(attraction=attraction).all()

    def getFeedbacks(self, trip):
        return FeedbackInstance.objects.filter(trip=trip).all()

    def getAmericanQuestion(self, attraction):
        return AmericanQuestion.objects.filter(attraction=attraction).first()

    def getAttraction(self, attrId):
        return Attraction.objects.filter(id=attrId).first()

    def getTrip(self, tripId):
        return Trip.objects.filter(id=tripId).first()

    def add_attraction(self, name, x, y, description, picturesURLS, videosURLS):
        attraction = Attraction(name=name, x=x, y=y, description=description, picturesURLS=picturesURLS,
                                videosURLS=videosURLS)
        attraction.save()
        return attraction

    def add_hint(self, id_attraction, kind, data):
        hint = Hint(attraction=self.getAttraction(id_attraction), kind=kind, data=data)
        hint.save()
        return hint

    def add_american_question(self, id_attraction, question, answers, indexOfCorrectAnswer):
        aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer,
                              attraction=self.getAttraction(id_attraction))
        aq.save()
        return aq

    def add_track(self, points, length):
        track = Track(length=length)
        track.save()
        for p in points:
            attr = self.get_attraction(p['id'])
            track.points.add(attr)
            track.save()
        return track

    def add_feedback_question(self, question, kind):
        feedback = Feedback(question=question, kind=kind)
        feedback.save()
        return feedback

    def get_track(self, track_len):
        return Track.objects.filter(length=track_len).all()

    def get_attraction(self, id):
        return Attraction.objects.get(pk=id)

    def get_attractions(self):
        return Attraction.objects.all()

    def getAllTracksThatIncludeThisTrack(self, track):
        return Track.objects.filter(subTrack=track).all()

    def delete_attraction(self, id):
        delt=self.get_attraction(id).delete()
        return True

    def edit_attraction(self, id, name, x, y, description, picturesURLS, videosURLS):
        attraction = self.get_attraction(id)
        attraction.name=name
        attraction.x=x
        attraction.y=y
        attraction.description=description
        attraction.picturesURLS=picturesURLS
        attraction.videosURLS=videosURLS
        attraction.save()
        return attraction

    def delete_american_question(self, id_attraction, id_a_question):
        aq = self.get_american_question(id_attraction, id_a_question).delete()
        return True

    def delete_hint(self, id_attraction, id_hint):
        hint = self.get_hint(id_attraction, id_hint).delete()
        return True

    def edit_hint(self, id_attraction, id_hint, data):
        hint = self.get_hint(id_attraction, id_hint)
        hint.data = data
        hint.save()
        return True

    def get_all_tracks(self):
        return Track.objects.all()

    def delete_feedback_question(self, id_feedback):
        feedback = self.get_feedback_question(id_feedback).delete()
        return True

    def get_american_question(self, id_attraction, id_american_question):
        return AmericanQuestion.objects.filter(pk=id_american_question,
                                               attraction=self.get_attraction(id_attraction)).first()

    def get_hint(self, id_attraction, id_hint):
        return Hint.objects.filter(pk=id_hint, attraction=self.getAttraction(id_attraction)).first()

    def get_feedback_question(self, id_feedback):
        return Feedback.objects.filter(pk=id_feedback).all()

    def get_attraction_by_x_y(self, x, y):
        return Attraction.objects.filter(x=x, y=y).first()

    def get_all_aquestions_for_attraction(self, id_attraction):
        return AmericanQuestion.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def get_all_hints_for_attraction(self, id_attraction):
        return Hint.objects.filter(attraction=self.get_attraction(id_attraction)).all()
