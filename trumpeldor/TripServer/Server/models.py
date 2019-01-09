from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Attraction(models.Model):
    # pointNumber = models.AutoField(primary_key=True)
    name = models.TextField(default='fake')
    x = models.FloatField()
    y = models.FloatField()
    description = models.TextField()
    picturesURLS = JSONField(blank=True, null=True)
    videosURLS = JSONField(blank=True, null=True)


class User(models.Model):
    name = models.TextField()
    socialNetwork = models.TextField()
    # playersAges = JSONField(null=True)
    lastSeen = models.DateTimeField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True) # To send user notifications in the mail

    class Meta:
        unique_together = (("name", "socialNetwork"),)


class Track(models.Model):
    # trackNumber = models.AutoField(primary_key=True)
    subTrack = models.ForeignKey('Track', on_delete=models.CASCADE, blank=True, null=True)
    points = models.ManyToManyField(Attraction)
    length = models.IntegerField()


class Trip(models.Model):
    # TripNumber = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groupName = models.TextField(default='fake')
    playersAges = JSONField(null=True)
    score = models.IntegerField(default=0)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    # nextAttraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, blank=True, null=True)
    attractionsDone = models.ManyToManyField(Attraction)    # First Attraction is the current attraction!!!!


class AmericanQuestion(models.Model):
    # americanQuestionNumber = models.AutoField(primary_key=True)
    question = models.TextField()
    answers = JSONField()  # Should be list of String
    indexOfCorrectAnswer = models.IntegerField()
    myAttraction = models.OneToOneField(Attraction, on_delete=models.CASCADE)  # null=True for migrations. need to think about it


class Entertainment(models.Model):
    entertainmentNumber = models.AutoField(primary_key=True)
    myAttraction = models.OneToOneField(Attraction, on_delete=models.CASCADE) # null=True for migrations. need to think about it

    class Meta:
        abstract = True
        unique_together = (("entertainmentNumber", "myAttraction"),)


class FindTheDifferences(Entertainment):
    pictureURL = models.TextField()
    differences = JSONField()  # Should be list of x's and y's (Location of each difference)


class Puzzle(Entertainment):
    pictureURL = models.TextField()


class SlidingPuzzle(Entertainment):
    piecesURLS = JSONField()  # Should be list of paths


class Feedback(models.Model):
    questionNumber = models.AutoField(primary_key=True)
    question = models.TextField()


class FeedbackInstance(models.Model):
    questionNumber = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE) # null=True for migrations. need to think about it

    class Meta:
        abstract = True
        unique_together = (("questionNumber", "trip"),)


class FeedbackRating(FeedbackInstance):
    rating = models.IntegerField()


class FeedbackText(FeedbackInstance):
    answer = models.TextField()


class Hint(models.Model):
    hintNumber = models.AutoField(primary_key=True)
    myAttraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)

    HINT_TEXT = 'HT'
    HINT_PICTURE = 'HP'
    HINT_VIDEO = 'HV'
    HINT_MAP = 'HM'
    HINT_KIND = (
        (HINT_TEXT, 'HintText'),
        (HINT_PICTURE, 'HintPicture'),
        (HINT_VIDEO, 'HintVideo'),
        (HINT_MAP, 'HintMap'),
    )
    kind = models.CharField(
        max_length=2,
        choices=HINT_KIND,
        default=HINT_TEXT,
    )

    data = models.TextField()

    class Meta:
        unique_together = (("hintNumber", "myAttraction"),)
        # abstract = True


# class HintPicture(Hint):
#     pass
#     picturePath = models.TextField()
#
#
# class HintText(Hint):
#     pass
#     text = models.TextField()
#
#
# class HintVideo(Hint):
#     pass
#     videoPath = models.TextField()
#
#
# class HintMap(Hint):
#     mapPicturePath = models.TextField()
