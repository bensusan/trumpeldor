from rest_framework import serializers
from .models import *


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'x', 'y', 'description', 'picturesURLS', 'videosURLS',)
        model = Attraction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork', 'lastSeen', 'email',)
        model = User


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('subTrack', 'points', 'length',)
        model = Track


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'groupName', 'playersAges', 'score', 'track', 'attractionsDone')
        model = Trip


class AmericanQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('question', 'answers', 'indexOfCorrectAnswer', 'myAttraction',)
        model = AmericanQuestion


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entertainmentNumber', 'myAttraction',)
        model = Entertainment


class FindTheDifferencesSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('pictureURL', 'differences',)
        model = FindTheDifferences


class PuzzleSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('pictureURL',)
        model = Puzzle


class SlidingPuzzleSerializer(EntertainmentSerializer):
    class Meta:
        fields = ('piecesURLS',)
        model = SlidingPuzzle


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('questionNumber', 'question',)
        model = Feedback


class FeedbackInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('questionNumber', 'trip',)
        model = Feedback


class FeedbackRatingSerializer(FeedbackInstanceSerializer):
    class Meta:
        fields = ('rating',)
        model = FeedbackRating


class FeedbackTextSerializer(FeedbackInstanceSerializer):
    class Meta:
        fields = ('answer',)
        model = FeedbackText


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('hintNumber', 'myAttraction', 'kind', 'data',)
        model = Hint


# class HintPictureSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('picturePath',)
#         model = HintPicture
#
#
# class HintTextSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('text',)
#         model = HintText
#
#
# class HintVideoSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('videoPath',)
#         model = HintVideo
#
#
# class HintMapSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('mapPicturePath',)
#         model = HintMap


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork',)
        model = User


class GetRelevantPreviousTripInformationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('groupName', 'playersAges',)
        model = Trip


class CreateTripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('user', 'groupName', 'playersAges')
        model = Trip

    trackLength = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
