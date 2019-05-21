from rest_framework import serializers
from .models import *


class AmericanQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'answers', 'indexOfCorrectAnswer')
        model = AmericanQuestion


class HintSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'kind', 'data', 'description',)
        model = Hint


class AttractionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'x', 'y', 'description', 'picturesURLS', 'videosURLS', 'visible')
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


class GetExtendedTrackSerializer(serializers.Serializer):
    trackId = serializers.IntegerField()
    x = serializers.FloatField()
    y = serializers.FloatField()


class TripSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    track = TrackSerializer()
    attractionsDone = AttractionSerializer(many=True)

    class Meta:
        fields = ('id', 'user', 'groupName', 'playersAges', 'score', 'track', 'attractionsDone')
        model = Trip

# class EntertainmentSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('id', 'attraction',)
#         model = Entertainment


class TakingPictureSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'description',)
        model = TakingPicture


class FindTheDifferencesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'description', 'pictureURL', 'differences',)
        model = FindTheDifferences


class PuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'description', 'piecesURLS', 'width', 'height',)
        model = Puzzle


class SlidingPuzzleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'description', 'piecesURLS', 'width', 'height',)
        model = SlidingPuzzle


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'question', 'kind',)
        model = Feedback


class FeedbackInstanceSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer()

    class Meta:
        fields = ('feedback', 'trip', 'answer')
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


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'data')
        model = Message


class UpdateTripSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user = UserSerializer()
    groupName = serializers.CharField(max_length=50)
    playersAges = serializers.JSONField()
    score = serializers.IntegerField()
    track = TrackSerializer()
    attractionsDone = AttractionSerializer(many=True)
    feedbacks = FeedbackInstanceSerializer(many=True)


class ScoreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('groupName', 'score')
        model = Trip


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'app_name', 'about_app', 'how_to_play',)
        model = Info


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('description', 'fileURL',)
        model = Media


class IsAdminSerializer(serializers.Serializer):
    email = serializers.EmailField()



class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('boundaries', 'logo', 'loginHours', 'successAudio', 'failureAudio',)
        model = Settings
