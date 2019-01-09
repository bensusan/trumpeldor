import null
import random

from django.shortcuts import render
from rest_framework.utils import json

from ..models import *
from django.http import JsonResponse, HttpResponse, Http404

from rest_framework import generics
from ..serializers import *
from rest_framework.views import APIView
from ..models import *

from .. import BL
from django.core import serializers


class AmericanQuestion(generics.ListCreateAPIView):     #need to change to Create without list
    queryset = AmericanQuestion.objects.all()
    serializer_class = AmericanQuestionSerializer


# class Attraction(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, xPoint, yPoint):
#         try:
#             return models.Attraction.objects.filter(x = xPoint and y = yPoint)
#         except models.Attraction.DoesNotExist:
#             raise Http404
#
#     def get(self, request, attrID, format=None):
#         attr = self.get_object(attrID)
#         serializer = AttractionSerializer(attr)
#         return JsonResponse(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AttractionSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
#     def put(self, request, attrID, format=None):
#         attr = self.get_object(attrID)
#         serializer = AttractionSerializer(attr, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors)
#
#     def delete(self, request, attrID, format=None):
#         attr = self.get_object(attrID)
#         attr.delete()
#         return JsonResponse()


class Attractions(APIView):

    def get(self, request, format=None):
        attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.data)
        serializer = AttractionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors)


class SpecificAttraction(APIView):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    def delete(self, request, xp, yp, format=None):
        print(xp +" " + yp)
        attr_del = Attraction.objects.filter(x=xp).filter(y=yp)
        attr_del.delete()
        return JsonResponse(attr_del.errors)


# class Hint(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hint.objects.all()
#     serializer_class = HintSerializer


class Feedback(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class SignIn(APIView):

    def get(self, request, format=None):
        return JsonResponse({'name': 'admin', 'password': '1234'})


def add_attraction_page(request):
    return render(request, "ManageSystem/addAttraction.html")

# def delete_attraction(request):
#     return render(request, "ManageSystem/addAttraction.html")
#
# def add_attraction(request):
#     return render(request, "ManageSystem/addAttraction.html")


def main_page(request):
    return render(request, "ManageSystem/MainPage.html")

def map_page(request):
    return render(request, "ManageSystem/map.html")

def map_track_page(request):
    return render(request, "ManageSystem/MapForTracks.html")

def add_AQ_page(request):
    return render(request, "ManageSystem/americanQuestion.html")

def checkIfPointExist(lat, lng):
    queryset = Attraction.objects.filter(x=lat).filter(y=lng)
    try:
        serializer = AttractionSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Attraction.DoesNotExist:
        raise Http404


class Tracks(APIView):

    def get(self, request, format=None):
        tracks = Track.objects.all()
        serializer = TrackSerializer(tracks, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        print(request.data['points'])
        serializer = TrackSerializer(data=request.data)
        for point in request.data['points']:
            serializer.points.add(point)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors)
