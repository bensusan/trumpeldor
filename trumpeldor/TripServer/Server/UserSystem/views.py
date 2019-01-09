import null
from rest_framework.response import Response
from django.http import Http404

from rest_framework import generics
from ..serializers import *
from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
import json

DAL_Impl = DAL_Implementation()
BL_Impl = BL_Implementation()
BL_Impl.setDAL(DAL_Impl)
BL = BLProxy()
BL.setImplementation(BL_Impl)

DEBUG = True


# General post for all the posts here
# blFunction must include only 1 argument (request.data)
def generalPost(request, className, blFunction, classSerializer, many=False):
    if DEBUG:
        print(className + ":", "Get:", request.data, sep="\n")
    ans = blFunction(request.data)
    ans = classSerializer(ans, many=many)
    ans = json.loads(json.dumps(ans.data))
    if DEBUG:
        print("Sent:", ans, sep="\n")
    return Response(ans)


class SignUp(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(request, "SignUp", BL.signUp, UserSerializer)


class PreviousTrip(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "PreviousTrip",
            BL.getPreviousUserTrip,
            TripSerializer)


class GetRelevantPreviousTripInformation(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetRelevantPreviousTripInformation",
            BL.getRelevantPreviousTripInformation,
            GetRelevantPreviousTripInformationSerializer)


class CreateTrip(generics.GenericAPIView):
    serializer_class = CreateTripSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "CreateTrip",
            BL.createTrip,
            TripSerializer)


class GetHints(generics.GenericAPIView):
    serializer_class = AttractionSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetHints",
            BL.getHints,
            HintSerializer,
            True)


class GetFeedbacks(generics.GenericAPIView):
    serializer_class = TripSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetFeedbacks",
            BL.getFeedbacks,
            FeedbackInstanceSerializer,
            True)


class GetAmericanQuestion(generics.GenericAPIView):
    serializer_class = AttractionSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetAmericanQuestion",
            BL.getAmericanQuestion,
            AmericanQuestionSerializer)


# class GetTrackById(generics.GenericAPIView):
#     serializer_class = IdSerializer
#
#     def post(self, request, *args, **kwargs):
#         return generalPost(
#             request,
#             "GetAmericanQuestion",
#             BL.getTrackById,
#             TrackSerializer)
#
#
# class GetAttractionsById(generics.GenericAPIView):
#     serializer_class = IdSerializer
#
#     def post(self, request, *args, **kwargs):
#         return generalPost(
#             request,
#             "GetAmericanQuestion",
#             BL.getAmericanQuestion,
#             AmericanQuestionSerializer)
#
#
# class GetAmericanQuestion(generics.GenericAPIView):
#     serializer_class = IdSerializer
#
#     def post(self, request, *args, **kwargs):
#         return generalPost(
#             request,
#             "GetAmericanQuestion",
#             BL.getAmericanQuestion,
#             AmericanQuestionSerializer)





def addFeedback(question, kind):
    feedback = Feedback(question=question, kind=kind)
    feedback.save()
    return feedback


def addHint(attraction, kind, data):
    hint = Hint(attraction=attraction, kind=kind, data=data)
    hint.save()
    return hint


def addAmericanQuestion(question, answers, indexOfCorrectAnswer, attraction):
    aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer, attraction=attraction)
    aq.save()
    return aq


def addTrack(subTrack, points, length):
    track = None
    if subTrack == null:
        track = Track(length=length)
    else:
        track = Track(subTrack=subTrack, length=length)
    track.save()
    for p in points:
        track.points.add(p)
    return track


def addAttraction(name, x, y, description, picturesURLS, videosURLS):
    attraction = Attraction(name=name, x=x, y=y, description=description, picturesURLS=picturesURLS, videosURLS=videosURLS)
    attraction.save()
    return attraction


def insertToDal(data):
    a1 = addAttraction("Attraction 1", "0.1", "0.1", "We Are in Attraction 1", ["x.jpg"], [])
    a2 = addAttraction("Attraction 2", "0.2", "0.2", "We Are in Attraction 2", ["y.png"], [])
    aq1 = addAmericanQuestion("AQ1: Some question here ?", ["Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 1, a1)
    aq2 = addAmericanQuestion("AQ2: Some question here ?", ["Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 2, a2)
    h11 = addHint(a1, Hint.HINT_TEXT, "This is text hint for Attraction 1")
    h12 = addHint(a1, Hint.HINT_PICTURE, "x.jpg")
    h13 = addHint(a1, Hint.HINT_MAP, "0.1,0.1")

    h21 = addHint(a2, Hint.HINT_PICTURE, "y.png")
    h22 = addHint(a2, Hint.HINT_TEXT, "This is text hint for Attraction 2")
    h23 = addHint(a2, Hint.HINT_MAP, "0.2,0.2")

    track1 = addTrack(null, [a1], 1)
    track2 = addTrack(null, [a2], 1)

    track12 = addTrack(track1, [a2], 2)

    f1 = addFeedback("Feedback 1 rating ??", Feedback.FEEDBACK_RATING)
    f2 = addFeedback("Feedback 2 text ??", Feedback.FEEDBACK_TEXT)
    return track12


class AddToDal(generics.GenericAPIView):
    serializer_class = TestSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetFeedbacks",
            insertToDal,
            TrackSerializer)
        # if DEBUG:
        #     print("AddToDal" + ":", "Got Message data:", request.data, sep="\n")
        # track = insertToDal()
        # serializer = TrackSerializer(track)
        # if DEBUG:
        #     print("Sent Message data:", serializer.data, sep="\n")
        # return Response(serializer.data)
