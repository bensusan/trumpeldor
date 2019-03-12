import null
import datetime
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
        feedbacks = self.getFeedbacks()
        for feedback in feedbacks:
            self.createFeedbackInstance(feedback, trip)
        return trip

    def doneAttractionInTrip(self, trip, newAttraction):
        trip.attractionsDone.add(newAttraction)

    def createUser(self, name, socialNetwork):
        user = User(name=name, socialNetwork=socialNetwork)
        user.save()
        return user

    def getHints(self, attraction):
        return Hint.objects.filter(attraction=attraction).all()

    def getFeedbacks(self):
        return Feedback.objects.all()

    def getFeedbackInstances(self, trip):
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

    def add_hint(self, attraction, kind, data):
        hint = Hint(attraction=attraction, kind=kind, data=data)
        hint.save()
        return hint

    def add_american_question(self, question, answers, indexOfCorrectAnswer, attraction):
        aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer,
                              attraction=attraction)
        aq.save()
        return aq

    def add_track(self, subTrack, points, length):
        track = None
        if subTrack == null:
            track = Track(length=length)
        else:
            track = Track(subTrack=subTrack, length=length)
        track.save()
        for p in points:
            track.points.add(p)
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

    def getOpenMessages(self):
        return Message.objects.all()

    def updateTrip(self, prevTrip, track, groupName, score, playersAges, attractionsDone):
        prevTrip.track = track
        prevTrip.groupName = groupName
        prevTrip.score = score
        prevTrip.playersAges = playersAges
        prevTrip.save()
        prevTrip.attractionsDone.clear()
        for attraction in attractionsDone:
            prevTrip.attractionsDone.add(attraction)
        return prevTrip

    def updateFeedbackInstance(self, feedback, trip, answer):
        prevFI = FeedbackInstance.objects.filter(trip=trip).filter(feedback=feedback).first()
        prevFI.answer = answer
        prevFI.save()

    def createFeedbackInstance(self, feedback, trip):
        fi = FeedbackInstance(feedback=feedback, trip=trip, answer="")
        fi.save()

    def getFeedbackById(self, feedbackId):
        return Feedback.objects.get(id=feedbackId)

    def updateLastSeenToNow(self, user):
        user.lastSeen = datetime.datetime.now()
        user.save()
        return user

    def getAllTrips(self):
        return Trip.objects.order_by('score')
