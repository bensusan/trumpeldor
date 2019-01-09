from rest_framework import serializers
from .models import *


class AmericanQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'answers', 'indexOfCorrectAnswer')
        model = AmericanQuestion


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'kind', 'data',)
        model = Hint


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'x', 'y', 'description', 'picturesURLS', 'videosURLS',)
        model = Attraction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork', 'lastSeen', 'email',)
        model = User


class TrackSerializer(serializers.ModelSerializer):
    subTrack = serializers.SerializerMethodField()
    points = AttractionSerializer(many=True)

    class Meta:
        fields = ('id', 'subTrack', 'points', 'length',)
        model = Track

    def get_subTrack(self, obj):
        if obj.subTrack is not None:
            return TrackSerializer(obj.subTrack).data
        else:
            return None


class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    track = TrackSerializer()
    attractionsDone = AttractionSerializer(many=True)

    class Meta:
        fields = ('id', 'user', 'groupName', 'playersAges', 'score', 'track', 'attractionsDone')
        model = Trip


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'attraction',)
        model = Entertainment


class FindTheDifferencesSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('id', 'pictureURL', 'differences',)
        model = FindTheDifferences


class PuzzleSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('id', 'pictureURL',)
        model = Puzzle


class SlidingPuzzleSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('id', 'piecesURLS',)
        model = SlidingPuzzle


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'kind',)
        model = Feedback


class FeedbackInstanceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer()

    class Meta:
        fields = ('feedback', 'trip',)
        model = FeedbackInstance


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork',)
        model = User


class GetRelevantPreviousTripInformationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('groupName', 'playersAges',)
        model = Trip


class CreateTripSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        fields = ('groupName', 'playersAges')
        model = Trip

    trackLength = serializers.IntegerField()
    x = serializers.FloatField()
    y = serializers.FloatField()

class TestSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('question',)
        model = Feedback