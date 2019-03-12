from django.db import models
from django.contrib.postgres.fields import JSONField

# we can see which type is every field
class Attraction(models.Model):
    name = models.TextField()
    x = models.FloatField()
    y = models.FloatField()
    description = models.TextField()
    picturesURLS = JSONField(blank=True, null=True)
    videosURLS = JSONField(blank=True, null=True)


class User(models.Model):
    name = models.TextField()
    socialNetwork = models.TextField()
    lastSeen = models.DateTimeField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)     # To send user notifications in the mail

    class Meta:
        unique_together = (("name", "socialNetwork"),)


class Track(models.Model):
    subTrack = models.ForeignKey('Track', on_delete=models.CASCADE, blank=True, null=True)
    points = models.ManyToManyField(Attraction)
    length = models.IntegerField()


class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groupName = models.TextField()
    playersAges = JSONField(null=True)
    score = models.IntegerField(default=0)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    attractionsDone = models.ManyToManyField(Attraction)    # First Attraction is the current attraction!!!!


class AmericanQuestion(models.Model):
    question = models.TextField()
    answers = JSONField()  # Should be list of String
    indexOfCorrectAnswer = models.IntegerField()
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)


class Entertainment(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)


class FindTheDifferences(Entertainment):
    pictureURL = models.TextField()
    differences = JSONField()  # Should be list of x's and y's (Location of each difference)


class Puzzle(Entertainment):
    pictureURL = models.TextField()


class SlidingPuzzle(Entertainment):
    piecesURLS = JSONField()  # Should be list of paths


class Feedback(models.Model):
    question = models.TextField()

    FEEDBACK_TEXT = 'FT'
    FEEDBACK_RATING = 'FR'
    FEEDBACK_KIND = (
        (FEEDBACK_TEXT, 'FeedbackText'),
        (FEEDBACK_RATING, 'FeedbackRating'),
    )
    kind = models.CharField(
        max_length=2,
        choices=FEEDBACK_KIND,
        default=FEEDBACK_TEXT,
    )


class FeedbackInstance(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    answer = models.TextField()

    class Meta:
        unique_together = (("feedback", "trip"),)


class Hint(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    HINT_TEXT = 'HT'
    HINT_PICTURE = 'HP'
    HINT_VIDEO = 'HV'
    HINT_KIND = (
        (HINT_TEXT, 'HintText'),            # "Something"
        (HINT_PICTURE, 'HintPicture'),      # "x.jpg"
        (HINT_VIDEO, 'HintVideo'),          # "x.mp4"
    )
    kind = models.CharField(
        max_length=2,
        choices=HINT_KIND,
        default=HINT_TEXT,
    )

    data = models.TextField()


class Message(models.Model):
    title = models.CharField(max_length=50)     # TODO - maybe change length
    data = models.CharField(max_length=500)     # TODO - maybe change length
