from rest_framework import serializers
from .models import *


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('pointNumber', 'x', 'y', 'description', 'picturesPaths', 'videosPaths',)
        model = Attraction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'socialNetwork', 'playersAges', 'lastSeen', 'email',)
        model = User


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('points',)
        model = Track


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('tripNumber', 'user', 'score', 'track',)
        model = Trip


class AmericanQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'americanQuestionNumber', 'question', 'answers', 'indexOfCorrectAnswer', 'myAttraction',)
        model = AmericanQuestion


class EntertainmentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entertainmentNumber', 'myAttraction',)
        model = Entertainment


class FindTheDifferencesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('picturePath', 'picturePath',)
        model = FindTheDifferences


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('puzzlePicturePath',)
        model = Puzzle


class SlidingPuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('piecesPaths',)
        model = SlidingPuzzle


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('questionNumber', 'trip', 'question',)
        model = Feedback


class FeedbackRatingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('rating',)
        model = FeedbackRating


class FeedbackTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('answer',)
        model = FeedbackText


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('hintNumber', 'myAttraction',)
        model = Hint


class HintPictureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('picturePath',)
        model = HintPicture


class HintTextSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('text',)
        model = HintText


class HintVideoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('videoPath',)
        model = HintVideo


class HintMapSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('mapPicturePath',)
        model = HintMap


# class FileSerializer(serializers.ModelSerializer):
#     class Meta():
#         fields = ('file',)
#         model = File
#
#
class FileNameSerializer(serializers.ModelSerializer):
    class Meta():
        fields = ('filename',)
        model = FilePath
