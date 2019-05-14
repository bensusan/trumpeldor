from django.shortcuts import render, redirect
from rest_framework.utils import json

import null
from rest_framework.response import Response
from django.http import Http404, HttpResponse

from rest_framework import generics
from ..serializers import *
from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation
import json
# from ..forms import *

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

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_sliding_puzzle(self.kwargs['id_attr'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_sliding_puzzle(self.kwargs['id_attr'], request.data)
        ans = SlidingPuzzleSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class PuzzleList(generics.GenericAPIView):
    serializer_class = PuzzleSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_puzzles_for_attraction(self.kwargs['id_attr'])
        ans = PuzzleSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_puzzle(self.kwargs['id_attr'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        ans = BL.add_puzzle(self.kwargs['id_attr'], request.data)
        ans = PuzzleSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)


class FindTheDifferencesList(generics.GenericAPIView):
    serializer_class = FindTheDifferencesSerializer
    queryset = ''

    def get(self, request, *args, **kwargs):
        ans = BL.get_all_find_the_differences_for_attraction(self.kwargs['id_attr'])
        ans = FindTheDifferencesSerializer(ans, many=True)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

    def delete(self, request, *args, **kwargs):
        ans = BL.delete_find_the_differences(self.kwargs['id_attr'])
        ans = json.loads(json.dumps(ans))
        return Response(ans)

    def post(self, request, *args, **kwargs):
        # if 'x' not in request.data:
        #     if not isinstance(request.data['x'], (int, long, float, complex)):
        #         return Response(False)
        # if 'y' not in request.data:
        #     return Response(False)
        ans = BL.add_find_the_differences(self.kwargs['id_attr'], request.data)
        ans = FindTheDifferencesSerializer(ans, many=False)
        ans = json.loads(json.dumps(ans.data))
        return Response(ans)

# def sign_in_page(request):
#     return render(request, "signIn.html")


# Create your views here.
def images_view(request):
    if request.method == 'POST':
        form = ImagesForm(request.POST, request.FILES)
        print(request.FILES)
        print(request.POST)
        if form.is_valid():
            print('1111')
            form.save()
            return redirect('success')
    # else:
    #     form = ImagesForm()
    return render(request, 'Images_Form.html', {'form': form})


def success(request):
    return HttpResponse('successfuly uploaded')


def failure(request):
    return HttpResponse('failed :(')
