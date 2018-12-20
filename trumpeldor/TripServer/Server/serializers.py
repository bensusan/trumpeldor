from rest_framework import serializers
from . import models


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pointNumber', 'x', 'y', 'description', 'picturesPaths', 'videosPaths',)
        model = models.Attraction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork', 'playersAges', 'lastSeen', 'email',)
        model = models.User


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('points',)
        model = models.Track


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('tripNumber', 'user', 'score', 'track',)
        model = models.Trip


class AmericanQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'americanQuestionNumber', 'question', 'answers', 'indexOfCorrectAnswer', 'myAttraction',)
        model = models.AmericanQuestion


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entertainmentNumber', 'myAttraction',)
        model = models.Entertainment


class FindTheDifferencesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('picturePath', 'picturePath',)
        model = models.FindTheDifferences


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('puzzlePicturePath',)
        model = models.Puzzle


class SlidingPuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('piecesPaths',)
        model = models.SlidingPuzzle


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('questionNumber', 'trip', 'question',)
        model = models.Feedback


class FeedbackRatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('rating',)
        model = models.FeedbackRating


class FeedbackTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('answer',)
        model = models.FeedbackText


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('hintNumber', 'myAttraction',)
        model = models.Hint


class HintPictureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('picturePath',)
        model = models.HintPicture


class HintTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text',)
        model = models.HintText


class HintVideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('videoPath',)
        model = models.HintVideo


class HintMapSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('mapPicturePath',)
        model = models.HintMap

