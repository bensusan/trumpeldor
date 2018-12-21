from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Attraction(models.Model):
    pointNumber = models.AutoField(primary_key=True)
    x = models.FloatField()
    y = models.FloatField()
    description = models.TextField()
    picturesPaths = JSONField()
    videosPaths = JSONField()


class User(models.Model):
    name = models.TextField()
    socialNetwork = models.TextField()
    playersAges = JSONField(blank=True)
    lastSeen = models.DateField(blank=True)
    email = models.EmailField(blank=True) # To send user notifications in the mail

    class Meta:
        unique_together = (("name", "socialNetwork"),)


class Track(models.Model):
    trackNumber = models.AutoField(primary_key=True)
    subTrack = models.ForeignKey('Track', on_delete=models.CASCADE, blank=True, null=True)
    points = models.ManyToManyField(Attraction)
    length = models.IntegerField()


class Trip(models.Model):
    TripNumber = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE)


class AmericanQuestion(models.Model):
    americanQuestionNumber = models.AutoField(primary_key=True)
    question = models.TextField()
    answers = JSONField()  # Should be list of String
    indexOfCorrectAnswer = models.IntegerField()
    myAttraction = models.OneToOneField(Attraction, on_delete=models.CASCADE)  # null=True for migrations. need to think about it


class Entertainment(models.Model):
    entertainmentNumber = models.AutoField(primary_key=True)
    myAttraction = models.OneToOneField(Attraction, on_delete=models.CASCADE) # null=True for migrations. need to think about it

    class Meta:
        abstract = True


class FindTheDifferences(Entertainment):
    picturePath = models.TextField()
    differences = JSONField()  # Should be list of x's and y's (Location of each difference)


class Puzzle(Entertainment):
    puzzlePicturePath = models.TextField()


class SlidingPuzzle(Entertainment):
    piecesPaths = JSONField()  # Should be list of paths


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

    class Meta:
        abstract = True


class HintPicture(Hint):
    picturePath = models.TextField()


class HintText(Hint):
    text = models.TextField()


class HintVideo(Hint):
    videoPath = models.TextField()


class HintMap(Hint):
    mapPicturePath = models.TextField()


# class File(models.Model):
#     file = models.FileField(blank=False, null=False)
#   # remark = models.CharField(max_length=20)
#   # timestamp = models.DateTimeField(auto_now_add=True)
#
#
class FilePath(models.Model):
    filename = models.TextField()