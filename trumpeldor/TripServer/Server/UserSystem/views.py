from rest_framework.response import Response
from rest_framework import generics, views
from ..serializers import *
from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
from Server.Services import insertDebugData
import json

DAL_Impl = DAL_Implementation()
BL_Impl = BL_Implementation()
BL_Impl.setDAL(DAL_Impl)
BL = BLProxy()
BL.setImplementation(BL_Impl)

DEBUG = False


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


def generalGet(className, blFunction, classSerializer=None, many=False):
    if DEBUG:
        print(className + ":")
    ans = blFunction()
    if (ans is not None) and (classSerializer is not None):
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


class IsAdmin(generics.GenericAPIView):
    serializer_class = IsAdminSerializer

    def post(self, request, *args, **kwargs):
        return generalPost(
            request,
            "GetAdmin",
            BL.isAdmin)


class GetSettings(views.APIView):
    def get(self, request):
        return generalGet(
            "GetSettings",
            BL.getSettings)
######################################################################################################
# ----------------------------------------Add Manual Data Part----------------------------------------
######################################################################################################


class InsertDebugData(views.APIView):
    def get(self, request):
        return generalGet(
            "InsertDebugData",
            insertDebugData,
            TrackSerializer)
