from re import sub

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

    def add_hint(self, id_attraction, kind, data):
        hint = Hint(attraction=self.getAttraction(id_attraction), kind=kind, data=data)
        hint.save()
        return hint

    def add_american_question(self, id_attraction, question, answers, indexOfCorrectAnswer):
        aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer,
                              attraction=self.getAttraction(id_attraction))
        aq.save()
        return aq

    def add_track(self, subTrack, points, length):
        # for i in range(4-length):
        #     track = Track(length=length+i)
        #     track.save()
        #     for p in points:
        #         attr = self.get_attraction(p['id'])
        #         track.points.add(attr)
        #         track.save()
        # return True
        for i in range(4 - length):
            track = None
            if subTrack is None:
                track = Track(length=length)
            else:
                # sub_track = self.get_track(subTrack['id'])
                track = Track(subTrack=subTrack, length=length+i)
            track.save()
            if i == 0:
                for p in points:
                    attr = self.get_attraction(p['id'])
                    track.points.add(attr)
                    track.save()
                subTrack = track
        return True

    def add_feedback_question(self, question, kind):
        feedback = Feedback(question=question, kind=kind)
        feedback.save()
        return feedback

    def get_track(self, id):
        track = Track.objects.filter(pk=id).first()
        return track

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

    def getSlidingPuzzle(self, attraction):
        return SlidingPuzzle.objects.filter(attraction=attraction).first()

    def delete_attraction(self, id):
        delt=self.getAttraction(id).delete()
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

    def add_attraction_to_track(self, id_track, id_attraction):
        # attr = self.getAttraction(id_attraction)
        # if attr is not None:
        #     track = self.get_track(id_track)
        #     len = track.length
        #     for i in range(len, 4):
        #         track = self.get_track_by_length(i)
        #         track.points.add(attr)
        #         track.save()
        #     return True
        attr = self.getAttraction(id_attraction)
        if attr is not None:
            track = self.get_track(id_track)
            track.points.add(attr)
            track.save()
            return True

    def delete_attraction_from_track(self, id_track, id_attraction):
        # attr = self.getAttraction(id_attraction)
        # if attr is not None:
        #     track = self.get_track(id_track)
        #     len = track.length
        #     for i in range(1, len+1):
        #         track = self.get_track_by_length(i)
        #         track.points.remove(attr)
        #         track.save()
        #     return True
        attr = self.getAttraction(id_attraction)
        if attr is not None:
            track = self.get_track(id_track)
            track.points.remove(attr)
            track.save()
            return True


    def delete_track(self, id_track):
        track = self.get_track(id_track).delete()
        return True

    def get_track_by_length(self, len):
        return Track.objects.filter(length=len).first()

    def edit_track(self, id_track, points):
        track = self.get_track(id_track)
        track.points.set(null)
        print(points)
        for p in points:
            attr = self.getAttraction(p['id'])
            track.points.add(attr)
        track.save()
        return track

    def get_all_feedback_questions(self):
        return Feedback.objects.all()