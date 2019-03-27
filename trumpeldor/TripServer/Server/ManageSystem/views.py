
from django.shortcuts import render
from rest_framework.utils import json

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

DEBUG = False


# General post for all the posts here
# blFunction must include only 1 argument (request.data)
def general_post_or_get(request, className, bl_function, classSerializer, many=False):
    if DEBUG:
        print(className + ":", "Get:", request.data, sep="\n")
    if request is not None:
        ans = bl_function(request.data)
    else:
        ans = bl_function()
    ans = classSerializer(ans, many=many)
    ans = json.loads(json.dumps(ans.data))
    if DEBUG:
        print("Sent:", ans, sep="\n")
    return Response(ans)


class HintsList(generics.GenericAPIView):
    serializer_class = HintSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_hints_for_attraction(self.kwargs['id_attr'])
        ans = HintSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        if DEBUG:
            print("Sent:", ans, sep="\n")
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_hint(self.kwargs['id_attr'], request.data)
        ans = HintSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class Hint(generics.GenericAPIView):
    serializer_class = HintSerializer

    def get(self, request, *args, **kwargs):
        ans = BL.get_hint(self.kwargs['id_attr'], self.kwargs['id_hint'])
        ans = HintSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_hint(self.kwargs['id_attr'], self.kwargs['id_hint'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def put(self, request, *args, **kwargs):
        ans = BL.edit_hint(self.kwargs['id_attr'], self.kwargs['id_hint'], request.data)
        ans = json.loads(json.dumps(ans))
        return Response(ans)


class Feedback(generics.GenericAPIView):
    serializer_class = TripSerializer

    def get(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "Feedbacks",
            BL.getFeedbacks,
            FeedbackInstanceSerializer,
            True)

    def post(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "GetFeedbacks",
            BL.getFeedbacks,
            FeedbackInstanceSerializer,
            True)


class AmericanQuestionsList(generics.GenericAPIView):
    serializer_class = AmericanQuestionSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_aquestions_for_attraction(self.kwargs['id_attr'])
        ans = AmericanQuestionSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        if DEBUG:
            print("Sent:", ans, sep="\n")
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_american_question(self.kwargs['id_attr'], request.data)
        ans = AmericanQuestionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class AmericanQuestion(generics.GenericAPIView):
    serializer_class = AmericanQuestionSerializer

    def get(self, request, *args, **kwargs):
        ans = BL.get_american_question(self.kwargs['id_attr'], self.kwargs['id_quest'])
        ans = AmericanQuestionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_american_question(self.kwargs['id_attr'], self.kwargs['id_quest'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_american_question(self.kwargs['id_attr'], request.data)
        ans = AmericanQuestionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class TracksList(generics.GenericAPIView):
    serializer_class = TrackSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_tracks()
        ans = TrackSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        if DEBUG:
            print("Sent:", ans, sep="\n")
        return Response(ans)

    def post(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "AddAttraction",
            BL.add_track,
            TrackSerializer)


class Track(generics.GenericAPIView):
    serializer_class = TrackSerializer

    def get(self, request, *args, **kwargs):
        ans = BL.get_track(self.kwargs['id'])
        ans = TrackSerializer(ans, many=False)
        ans = json.dumps(ans.data)
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_track(self.kwargs['id'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def put(self, request, *args, **kwargs):
        if self.kwargs['action'] == 'del':
            ans = BL.delete_attraction_from_track(self.kwargs['id'], request.data)
        elif self.kwargs['action'] == "add":
            ans = BL.add_attraction_to_track(self.kwargs['id'], request.data)
        ans = json.loads(json.dumps(ans))
        return Response(ans)


class AttractionsList(generics.GenericAPIView):
    serializer_class = AttractionSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        # ans = BL.get_attractions()
        # ans = AttractionSerializer(ans, many=True)
        # ans = json.loads(json.dumps(ans.data))
        # if DEBUG:
        #     print("Sent:", ans, sep="\n")
        # return Response(ans)
        return general_post_or_get(
            None,
            "AddAttraction",
            BL.get_attractions,
            AttractionSerializer,
            True)

    def post(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "AddAttraction",
            BL.add_attraction,
            AttractionSerializer)


class Attraction(generics.GenericAPIView):
    serializer_class = AttractionSerializer

    def get(self, request, *args, **kwargs):
        ans =BL.get_attraction(self.kwargs['id'])
        ans = AttractionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_attraction(self.kwargs['id'])
        ans = AttractionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def put(self, request, *args, **kwargs):
        ans = BL.edit_attraction(self.kwargs['id'], request.data)
        ans = AttractionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class EntertainmentsList(generics.GenericAPIView):
    serializer_class = EntertainmentSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        return general_post_or_get(
            None,
            "AddAttraction",
            BL.get_attractions,
            AttractionSerializer,
            True)

    def post(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "AddAttraction",
            BL.add_attraction,
            AttractionSerializer)

def sign_in_page(request):
    return render(request, "signIn.html")

def manage_attractions_page(request):
    return render(request, "attractions.html")

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



