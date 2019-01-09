from rest_framework.response import Response
from rest_framework.views import APIView
import random
from django.http import JsonResponse, HttpResponse, Http404

from rest_framework import generics
from ..serializers import *
from .. import BL
from django.core import serializers
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


class AmericanQuestion(generics.RetrieveAPIView):
    serializer_class = AmericanQuestionSerializer

    def get_object(self, pointId):

        try:
            questions = AmericanQuestion.objects.filter(myAttraction=pointId)
            numOfQuestions = questions.count()
            pk = random.randint(0, numOfQuestions)
            return questions[pk]
        except AmericanQuestion.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        question = self.get_object(pk)
        serializer = AmericanQuestionSerializer(question)
        return HttpResponse(serializer.data)


class Hint(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self, pk):

        try:
            return Hint.objects.get(pk=pk)
        except Hint.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        hint = self.get_object(pk)
        serializer = HintSerializer(hint)
        return HttpResponse(serializer.data)


class GetClass(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)


class SignUp(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        print("SignUp:", "Got Message data:", request.data, sep="\n")
        user = BL.getUser(request.data)
        if user is None:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = BL.getUser(request.data)
            else:
                print("Bug in SignUp method")
                raise Http404

        serializer = UserSerializer(user)
        print("SignUp:", "Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)


class GetTrack(generics.RetrieveAPIView):
    serializer_class = TrackSerializer

    def get_object(self, pk):

        try:
            tracks = Track.objects.filter(len=pk)
            numOftracks = tracks.count()
            pk = random.randint(0, numOftracks)
            return tracks.objects.get(pk=pk)
        except Track.DoesNotExist:
            raise Http404


class PreviousTrip(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        print("PreviousTrip:", "Got Message data:", request.data, sep="\n")
        trip = BL.getPreviousUserTrip(request.data)
        if trip is None:
            print("Bug in PreviousTrip method (Trip does not exist)")
            raise Http404

        serializer = TripSerializer(trip)
        print("PreviousTrip:", "Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)
