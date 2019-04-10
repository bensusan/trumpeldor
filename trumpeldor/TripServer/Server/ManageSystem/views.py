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


class FeedbackList(generics.GenericAPIView):
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_feedback_questions()
        ans = FeedbackSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_feedback_question(request.data)
        ans = FeedbackSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class Feedback(generics.GenericAPIView):
    serializer_class = FeedbackSerializer

    def get(self, request, *args, **kwargs):
        ans = BL.get_feedback_question(self.kwargs['id'])
        ans = FeedbackSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_feedback_question(self.kwargs['id'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)


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
        ans = BL.add_track(request.data)
        ans = json.loads(json.dumps(ans))
        return Response(ans)


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
        #ans = AttractionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def put(self, request, *args, **kwargs):
        ans = BL.edit_attraction(self.kwargs['id'], request.data)
        ans = AttractionSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class Info(generics.GenericAPIView):
    serializer_class = InfoSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_info()
        ans = InfoSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        return general_post_or_get(
            request,
            "AddAttraction",
            BL.add_info,
            InfoSerializer)


class InfoSpecific(generics.GenericAPIView):
    serializer_class = InfoSerializer

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_info(self.kwargs['id'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)


class SlidingPuzzleList(generics.GenericAPIView):
    serializer_class = SlidingPuzzleSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_sliding_puzzles_for_attraction(self.kwargs['id_attr'])
        ans = SlidingPuzzleSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_sliding_puzzle(self.kwargs['id_attr'], request.data)
        ans = SlidingPuzzleSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

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





# class AmericanQuestion(generics.ListCreateAPIView):     #need to change to Create without list
#     queryset = AmericanQuestion.objects.all()
#     serializer_class = AmericanQuestionSerializer
#
#
#
#
# # class Attraction(APIView):
# #     """
# #     Retrieve, update or delete a snippet instance.
# #     """
# #     def get_object(self, xPoint, yPoint):
# #         try:
# #             return models.Attraction.objects.filter(x = xPoint and y = yPoint)
# #         except models.Attraction.DoesNotExist:
# #             raise Http404
# #
# #     def get(self, request, attrID, format=None):
# #         attr = self.get_object(attrID)
# #         serializer = AttractionSerializer(attr)
# #         return JsonResponse(serializer.data)
# #
# #     def post(self, request, format=None):
# #         serializer = AttractionSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors)
# #
# #     def put(self, request, attrID, format=None):
# #         attr = self.get_object(attrID)
# #         serializer = AttractionSerializer(attr, data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return JsonResponse(serializer.data)
# #         return JsonResponse(serializer.errors)
# #
# #     def delete(self, request, attrID, format=None):
# #         attr = self.get_object(attrID)
# #         attr.delete()
# #         return JsonResponse()
#
#
# class Attractions(APIView):
#
#     def get(self, request, format=None):
#         attractions = Attraction.objects.all()
#         serializer = AttractionSerializer(attractions, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, format=None):
#         print(request.data)
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors)
#
#
# class SpecificAttraction(APIView):
#     queryset = Attraction.objects.all()
#     serializer_class = AttractionSerializer
#
#     def delete(self, request, xp, yp, format=None):
#         print(xp +" " + yp)
#         attr_del = Attraction.objects.filter(x=xp).filter(y=yp)
#         attr_del.delete()
#         return JsonResponse(attr_del.errors)
#
#
# # class Hint(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Hint.objects.all()
# #     serializer_class = HintSerializer
#
#
# class Feedback(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     queryset = Feedback.objects.all()
#     serializer_class = FeedbackSerializer
#
#
# class SignIn(APIView):
#
#     def get(self, request, format=None):
#         return JsonResponse({'name': 'admin', 'password': '1234'})
#
#
# def add_attraction_page(request):
#     return render(request, "ManageSystem/addAttraction.html")
#
# # def delete_attraction(request):
# #     return render(request, "ManageSystem/addAttraction.html")
# #
# # def add_attraction(request):
# #     return render(request, "ManageSystem/addAttraction.html")
#
#
# def main_page(request):
#     return render(request, "ManageSystem/MainPage.html")
#
# def map_page(request):
#     return render(request, "ManageSystem/map.html")
#
# def map_track_page(request):
#     return render(request, "ManageSystem/MapForTracks.html")
#
# def add_AQ_page(request):
#     return render(request, "ManageSystem/americanQuestion.html")
#
# def checkIfPointExist(lat, lng):
#     queryset = Attraction.objects.filter(x=lat).filter(y=lng)
#     try:
#         serializer = AttractionSerializer(queryset, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     except Attraction.DoesNotExist:
#         raise Http404
#
#
# class Tracks(APIView):
#
#     def get(self, request, format=None):
#         tracks = Track.objects.all()
#         serializer = TrackSerializer(tracks, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     def post(self, request, format=None):
#         print(request.data['points'])
#         serializer = TrackSerializer(data=request.data)
#         for point in request.data['points']:
#             serializer.points.add(point)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, safe=False)
#         return JsonResponse(serializer.errors)

