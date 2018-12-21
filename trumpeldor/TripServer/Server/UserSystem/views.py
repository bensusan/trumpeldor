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


class SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = BL.getUser(request.data)
        if user is None:
            seri = UserSerializer(data=request.data)
            if seri.is_valid():
                seri.save()
                user = BL.getUser(request.data)
            else:
                print("Bug in SignUp method")
        return HttpResponse(serializers.serialize('json', user), content_type='application/json')


# class FileView(APIView):
#     parser_classes = (MultiPartParser, FormParser)
#
#     def post(self, request, *args, **kwargs):
#         file_serializer = FileSerializer(data=request.data)
#         if file_serializer.is_valid():
#             file_serializer.save()
#             return Response(file_serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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


class GetFile(generics.CreateAPIView):
    serializer_class = FileNameSerializer

    def create(self, request, **kwargs):
        filename = request.data['filename']
        print(filename)
        # filename = 'x.jpg'
        file = open(filename, 'rb')
        response = HttpResponse(file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
#
# class X(APIView):
#     serializer_class = FileNameSerializer
#
#     def get(self, request, **kwargs):
#         # filename = request.data['filename']
#         # print(filename)
#         filename = 'x.jpg'
#         file = open(filename, 'rb')
#         response = HttpResponse(file, content_type='application/force-download')
#         response['Content-Disposition'] = 'attachment; filename="%s"' % filename
#         return response