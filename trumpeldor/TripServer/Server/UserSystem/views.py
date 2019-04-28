import sys
import null
from rest_framework.response import Response
from django.http import Http404

from rest_framework import generics, views
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
def generalPost(request, className, blFunction, classSerializer=None, many=False):
    if DEBUG:
        print(className + ":", "Get:", request.data, sep="\n")
    ans = blFunction(request.data)
    if (ans is not None) and (classSerializer is not None):
        ans = classSerializer(ans, many=many)
        ans = json.loads(json.dumps(ans.data))
    if DEBUG:
        print("Sent:", ans, sep="\n")
    return Response(ans)


def generalGet(className, blFunction, classSerializer, many=False):
    if DEBUG:
        print(className + ":")
    ans = blFunction()
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


class GetFeedbackInstances(generics.GenericAPIView):
    serializer_class = TripSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetFeedbackInstances",
            BL.getFeedbackInstances,
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


class GetExtendedTrack(generics.GenericAPIView):
    serializer_class = GetExtendedTrackSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetExtendedTrack",
            BL.getExtendedTrack,
            TrackSerializer)


class GetAttractionForDebug(views.APIView):

    def get(self, request):
        qs = Attraction.objects.first()
        ans = AttractionSerializer(qs)
        ans = json.loads(json.dumps(ans.data))
        if DEBUG:
            print("Sent:", ans, sep="\n")
        return Response(ans)


class GetOpenMessages(views.APIView):

    def get(self, request):
        return generalGet(
            "GetOpenMessages",
            BL.getOpenMessages,
            MessageSerializer,
            True)


class UpdateTrip(generics.GenericAPIView):
    serializer_class = UpdateTripSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "UpdateTrip",
            BL.updateTrip)


class GetBestScores(views.APIView):
    def get(self, request):
        return generalGet(
            "GetBestScores",
            BL.getBestScores,
            ScoreSerializer,
            True)


class GetEntertainment(generics.GenericAPIView):
    serializer_class = AttractionSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetEntertainment",
            BL.getEntertainment)
######################################################################################################
# ----------------------------------------Add Manual Data Part----------------------------------------
######################################################################################################


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


def addMessage(title, data):
    message = Message(title=title, data=data)
    message.save()
    return message


def addUser(userName, socialNetwork):
    user = User(name=userName, socialNetwork=socialNetwork)
    user.save()
    return user


def addSlidingPuzzle(attraction, width, height, listOfPicturesNames):
    sp = SlidingPuzzle(attraction=attraction, width=width, height=height, piecesURLS=listOfPicturesNames)
    sp.save()
    return sp

URL_PREFIX_MEDIA = "http://" + sys.argv[-1] + "/media/"


def addPrefixUrlToSpecificName(name):
    return URL_PREFIX_MEDIA + name


def addPrefixUrl(lst):
    newLst = []
    for name in lst:
        newLst += [addPrefixUrlToSpecificName(name)]
    return newLst

def insertDebugData():
    a1 = addAttraction("Meonot dalet", "31.263913", "34.796959", "We Are in Attraction 1", addPrefixUrl(["meonot_dalet_1.jpg", "meonot_dalet_2.jpg"]), [])
    a2 = addAttraction("96 building", "31.264934", "34.802062", "We Are in Attraction 2", addPrefixUrl(["96_1.jpg"]), [])
    a3 = addAttraction("Shnizale", "31.265129", "34.801575", "We Are in Attraction 3", addPrefixUrl(["shnizale_1.jpg", "shnizale_2.jpg"]), addPrefixUrl(["shnizale_video.mp4"]))
    aq1 = addAmericanQuestion("AQ1: Some question here ?", ["Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 0, a1)
    aq2 = addAmericanQuestion("AQ2: Some question here ?", ["Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 1, a2)
    aq3 = addAmericanQuestion("AQ3: Some question here ?", ["Incorrect answer",
                                                            "Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer"], 2, a3)

    sp1 = addSlidingPuzzle(a1, 3, 3,addPrefixUrl(["example00.jpg",
                                                  "example01.jpg",
                                                  "example02.jpg",
                                                  "example10.jpg",
                                                  "example11.jpg",
                                                  "example12.jpg",
                                                  "example20.jpg",
                                                  "example21.jpg",
                                                  "example22.jpg"]))

    sp2 = addSlidingPuzzle(a2, 3, 3, addPrefixUrl(["example00.jpg",
                                                   "example01.pg",
                                                   "example02.jpg",
                                                   "example10.jpg",
                                                   "example11.jpg",
                                                   "example12.jpg",
                                                   "example20.jpg",
                                                   "example21.jpg",
                                                   "example22.jpg"]))

    sp3 = addSlidingPuzzle(a3, 3, 3, addPrefixUrl(["example00.jpg",
                                                   "example01.jpg",
                                                   "example02.jpg",
                                                   "example10.jpg",
                                                   "example11.jpg",
                                                   "example12.jpg",
                                                   "example20.jpg",
                                                   "example21.jpg",
                                                   "example22.jpg"]))

    h11 = addHint(a1, Hint.HINT_TEXT, "This is text hint for Attraction 1")
    h12 = addHint(a1, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("meonot_dalet_1.jpg"))
    h13 = addHint(a1, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"))

    h21 = addHint(a2, Hint.HINT_TEXT, "This is text hint for Attraction 2")
    h22 = addHint(a2, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("96_1.jpg"))
    h23 = addHint(a2, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"))

    h31 = addHint(a3, Hint.HINT_TEXT, "This is text hint for Attraction 3")
    h32 = addHint(a3, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("shnizale_1.jpg"))
    h33 = addHint(a3, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"))

    track1 = addTrack(null, [a1], 1)
    track2 = addTrack(null, [a2], 1)
    track3 = addTrack(null, [a3], 1)

    track12 = addTrack(track1, [a2], 2)
    track13 = addTrack(track1, [a3], 2)
    track23 = addTrack(track2, [a3], 2)

    track123 = addTrack(track12, [a3], 3)

    f1 = addFeedback("Feedback 1 rating ?", Feedback.FEEDBACK_RATING)
    f2 = addFeedback("Feedback 2 text ?", Feedback.FEEDBACK_TEXT)

    msg1 = addMessage("Title for message 1", "data for message 1")
    msg2 = addMessage("Title for message 2", "data for message 2")

    anonymousUser = addUser("", "")
    return track123


class InsertDebugData(views.APIView):

    def get(self, request):
        return generalGet(
            "InsertDebugData",
            insertDebugData,
            TrackSerializer)
