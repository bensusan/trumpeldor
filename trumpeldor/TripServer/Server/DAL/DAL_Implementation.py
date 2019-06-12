import sys

import null
import datetime
from Server.models import *
from .DAL import DAL_Abstract
import base64
import uuid
import os.path
import image_slicer

class DAL_Implementation(DAL_Abstract):

    def getUser(self, name, socialNetwork):
        return User.objects.filter(name=name, socialNetwork=socialNetwork).first()

    def getPreviousTripByUser(self, name, socialNetwork):
        return Trip.objects.filter(user=self.getUser(name, socialNetwork)).last()

    def getTrackById(self, trackId):
        return Track.objects.filter(id=trackId).first()

    def getTracksWithSameLength(self, trackLength):
        return Track.objects.filter(length=trackLength).all()

    def createTrip(self, user, groupName, playersAges, track, attraction):
        trip = Trip(user=user, groupName=groupName, playersAges=playersAges, track=track)
        trip.save()
        self.doneAttractionInTrip(trip, attraction)
        feedbacks = self.getFeedbacks()
        for feedback in feedbacks:
            self.createFeedbackInstance(feedback, trip)
        return trip

    def doneAttractionInTrip(self, trip, newAttraction):
        trip.attractionsDone.add(newAttraction)

    def createUser(self, name, socialNetwork):
        user = User(name=name, socialNetwork=socialNetwork)
        user.save()
        return user

    def getHints(self, attraction):
        return Hint.objects.filter(attraction=attraction).all()

    def getFeedbacks(self):
        return Feedback.objects.all()

    def getFeedbackInstances(self, trip):
        return FeedbackInstance.objects.filter(trip=trip).all()

    def getAmericanQuestion(self, attraction):
        return AmericanQuestion.objects.filter(attraction=attraction).first()

    def getAttraction(self, attrId):
        return Attraction.objects.filter(id=attrId).first()

    def getTrip(self, tripId):
        return Trip.objects.filter(id=tripId).first()

    def getAdmins(self):
        # TODO!!!!!
        return ['kaplan.amit@gmail.com']

    def getSettings(self):
        return  {
                    'boundaries':   [
                                        {'x': 31.265372, 'y': 34.798240},
                                        {'x': 31.261009, 'y': 34.798178},
                                        {'x': 31.260975, 'y': 34.805906},
                                        {'x': 31.263513, 'y': 34.805998},
                                        {'x': 31.265315, 'y': 34.803155}
                                    ],
                    'logo':         addPrefixUrlToSpecificName("logo.png"),
                    'loginHours':   36,
                    'scoreRules':   [
                                        {'ruleName': 'hmtt', 'score': -10},
                                        {'ruleName': 'aqm', 'score': -2},
                                        {'ruleName': 'aqc', 'score': 10},
                                        {'ruleName': 'aa', 'score': 50},
                                        {'ruleName': 'sps', 'score': 10},
                                        {'ruleName': 'ttd', 'score': 10},
                                        {'ruleName': 'ps', 'score': 10}
                                    ]

                }

    def add_attraction(self, name, x, y, description, picturesURLS, videosURLS):
        names_of_pics=[]
        names_of_vids=[]
        if picturesURLS != 'null':
            names_of_pics = add_media(picturesURLS, 'image/jpeg', '.png')
        if videosURLS != 'null':
            names_of_vids = add_media(videosURLS, 'video/mp4', '.mp4')
        attraction = Attraction(name=name, x=x, y=y, description=description, picturesURLS=addPrefixUrl(names_of_pics),
                                videosURLS=addPrefixUrl(names_of_vids))
        attraction.save()
        return attraction

    def add_hint(self, id_attraction, kind, data, description):
        if kind == 'HP':
            data = add_media([data], 'image/jpeg', '.png')
        elif kind == 'HV':
            data = add_media([data], 'video/mp4', '.mp4')
        hint = Hint(attraction=self.getAttraction(id_attraction), kind=kind, data=addPrefixUrl(data)[0], description=description)
        hint.save()
        return hint

    def add_american_question(self, id_attraction, question, answers, indexOfCorrectAnswer):
        arr_correct_answers=[]
        for ind in indexOfCorrectAnswer:
            index = int(ind)-1
            arr_correct_answers.append(index)
        aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=arr_correct_answers,
                              attraction=self.getAttraction(id_attraction))
        aq.save()
        return aq

    def add_track(self, subTrack, points, length):
        # for i in range(4-length):
        #     track = Track(length=length+i)
        #     track.save()
        #     for p in points:
        #         attr = self.get_attraction(p['id'])
        #         track.points.add(attr)
        #         track.save()
        # return True
        for i in range(4 - length):
            track = None
            if subTrack is None:
                track = Track(length=length)
            else:
                # sub_track = self.get_track(subTrack['id'])
                track = Track(subTrack=subTrack, length=length+i)
            track.save()
            if i == 0:
                for p in points:
                    attr = self.get_attraction(p['id'])
                    track.points.add(attr)
                    track.save()
            subTrack = track
        return True

    def add_feedback_question(self, question, kind):
        feedback = Feedback(question=question, kind=kind)
        feedback.save()
        return feedback

    def get_track(self, id):
        track = Track.objects.filter(pk=id).first()
        return track

    def get_attraction(self, id):
        return Attraction.objects.get(pk=id)

    def get_attractions(self):
        return Attraction.objects.all()

    def getAllTracksThatIncludeThisTrack(self, track):
        return Track.objects.filter(subTrack=track).all()

    def getOpenMessages(self):
        return Message.objects.all()

    def updateTrip(self, prevTrip, track, groupName, score, playersAges, attractionsDone):
        prevTrip.track = track
        prevTrip.groupName = groupName
        prevTrip.score = score
        prevTrip.playersAges = playersAges
        prevTrip.save()
        prevTrip.attractionsDone.clear()
        for attraction in attractionsDone:
            prevTrip.attractionsDone.add(attraction)
        return prevTrip

    def updateFeedbackInstance(self, feedback, trip, answer):
        prevFI = FeedbackInstance.objects.filter(trip=trip).filter(feedback=feedback).first()
        prevFI.answer = answer
        prevFI.save()

    def createFeedbackInstance(self, feedback, trip):
        fi = FeedbackInstance(feedback=feedback, trip=trip, answer="")
        fi.save()

    def getFeedbackById(self, feedbackId):
        return Feedback.objects.get(id=feedbackId)

    def updateLastSeenToNow(self, user):
        user.lastSeen = datetime.datetime.now()
        user.save()
        return user

    def getAllTrips(self):
        return Trip.objects.order_by('score')

    def getSlidingPuzzle(self, attraction):
        return SlidingPuzzle.objects.filter(attraction=attraction).first()

    def getPuzzle(self, attraction):
        return Puzzle.objects.filter(attraction=attraction).first()

    def getTakingPicture(self, attraction):
        return TakingPicture.objects.filter(attraction=attraction).first()

    def delete_attraction(self, id):
        delt=self.getAttraction(id).delete()
        return True

    def edit_attraction(self, id, name, x, y, description, picturesURLS, videosURLS):
        attraction = self.get_attraction(id)
        attraction.name=name
        attraction.x=x
        attraction.y=y
        attraction.description=description
        if picturesURLS is not None:
            attraction.picturesURLS=addPrefixUrl(add_media(picturesURLS, 'image/jpeg', '.png'))
        if videosURLS is not None:
            attraction.videosURLS=addPrefixUrl(add_media(videosURLS, 'video/mp4', '.mp4'))
        attraction.save()
        return attraction

    def delete_american_question(self, id_attraction, id_a_question):
        aq = self.get_american_question(id_attraction, id_a_question).delete()
        return True

    def delete_hint(self, id_attraction, id_hint):
        hint = self.get_hint(id_attraction, id_hint).delete()
        return True

    def edit_hint(self, id_attraction, id_hint, data):
        hint = self.get_hint(id_attraction, id_hint)
        hint.data = data
        hint.save()
        return True

    def get_all_tracks(self):
        return Track.objects.all()

    def delete_feedback_question(self, id_feedback):
        feedback = self.get_feedback_question(id_feedback).delete()
        return True

    def get_american_question(self, id_attraction, id_american_question):
        return AmericanQuestion.objects.filter(pk=id_american_question,
                                               attraction=self.get_attraction(id_attraction)).first()

    def get_hint(self, id_attraction, id_hint):
        return Hint.objects.filter(pk=id_hint, attraction=self.getAttraction(id_attraction)).first()

    def get_feedback_question(self, id_feedback):
        return Feedback.objects.filter(pk=id_feedback).first()

    def get_attraction_by_x_y(self, x, y):
        return Attraction.objects.filter(x=x, y=y).first()

    def get_all_aquestions_for_attraction(self, id_attraction):
        return AmericanQuestion.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def get_all_hints_for_attraction(self, id_attraction):
        return Hint.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def add_attraction_to_track(self, id_track, id_attraction):
        # attr = self.getAttraction(id_attraction)
        # if attr is not None:
        #     track = self.get_track(id_track)
        #     len = track.length
        #     for i in range(len, 4):
        #         track = self.get_track_by_length(i)
        #         track.points.add(attr)
        #         track.save()
        #     return True
        attr = self.getAttraction(id_attraction)
        if attr is not None:
            track = self.get_track(id_track)
            track.points.add(attr)
            track.save()
            return True

    def delete_attraction_from_track(self, id_track, id_attraction):
        # attr = self.getAttraction(id_attraction)
        # if attr is not None:
        #     track = self.get_track(id_track)
        #     len = track.length
        #     for i in range(1, len+1):
        #         track = self.get_track_by_length(i)
        #         track.points.remove(attr)
        #         track.save()
        #     return True
        attr = self.getAttraction(id_attraction)
        track = self.get_track(id_track)
        if attr is not None:
            for i in range(1, track.length):
                track_smaller = self.get_track_by_length(i)
                print(i)
                print(track_smaller)
                print(track_smaller.points.all())
                print(attr)
                if attr in track_smaller.points.all():
                    return False
            track.points.remove(attr)
            track.save()
            return True


    def delete_track(self, id_track):
        track = self.get_track(id_track).delete()
        return True

    def get_track_by_length(self, len):
        return Track.objects.filter(length=len).first()

    def edit_track(self, id_track, points):
        track = self.get_track(id_track)
        track.points.set(null)
        for p in points:
            attr = self.getAttraction(p['id'])
            track.points.add(attr)
        track.save()
        return track

    def get_all_feedback_questions(self):
        return Feedback.objects.all()

    def add_info(self, app_name, about_app, how_to_play):
        info = Info(app_name=app_name, about_app=about_app,  how_to_play=how_to_play)
        info.save()
        if Info.objects.all().count() > 1:
            Info.objects.first().delete()
        return info

    def get_info(self):
        return Info.objects.last()

    def delete_info(self):
        return False

    def get_all_sliding_puzzles_for_attraction(self, id_attraction):
        return SlidingPuzzle.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def add_sliding_puzzle(self, id_attraction, piecesURLS, width, height, description):
        sliding_puzzle_pic = add_media([piecesURLS], 'image/jpeg', '.png')
        wid = int(width)
        hei = int(height)
        slicers = image_slicer.slice('media/' + sliding_puzzle_pic[0], wid*hei)
        tiles = []
        for tile in slicers:
            tile.filename = tile.filename.replace('media\\', '')
            tiles += [tile.filename]
        piceseURL = addPrefixUrl(tiles)
        sliding_puzzle = SlidingPuzzle(attraction=self.get_attraction(id_attraction), description=description, piecesURLS=piceseURL, width=wid, height=hei)
        sliding_puzzle.save()
        return sliding_puzzle

    def delete_sliding_puzzle(self, id_attraction):
        self.get_all_sliding_puzzles_for_attraction(id_attraction).delete()
        return True

    def get_all_puzzles_for_attraction(self, id_attraction):
        return Puzzle.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def add_puzzle(self, id_attraction, piecesURLS, width, height, description):
        puzzle_pic = add_media([piecesURLS], 'image/jpeg', '.png')
        wid = int(width)
        hei = int(height)
        slicers = image_slicer.slice('media/' + puzzle_pic[0], wid * hei)
        tiles = []
        for tile in slicers:
            tile.filename = tile.filename.replace('media\\', '')
            tiles += [tile.filename]
        piecesURLS = addPrefixUrl(tiles)
        puzzle = Puzzle(attraction=self.get_attraction(id_attraction), description=description,
                        piecesURLS=piecesURLS, width=width, height=height)
        puzzle.save()
        return puzzle

    def delete_puzzle(self, id_attraction):
        self.get_all_puzzles_for_attraction(id_attraction).delete()
        return True

    def get_all_find_the_differences_for_attraction(self, id_attraction):
        return FindTheDifferences.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def add_find_the_differences(self, id_attraction, pictureURL, differences, description):
        find_the_differences = FindTheDifferences(attraction=self.get_attraction(id_attraction), description=description,
                        pictureURL=pictureURL, differences=differences)
        find_the_differences.save()
        return find_the_differences

    def delete_find_the_differences(self, id_attraction):
        self.get_all_find_the_differences_for_attraction(id_attraction).delete()
        return True

    def taking_pic_exists(self, id_attraction):
        return TakingPicture.objects.filter(attraction=self.get_attraction(id_attraction)).all()

    def delete_taking_pic(self, id_attraction):
        self.taking_pic_exists(id_attraction).delete()
        return True

    def add_taking_pic(self, id_attraction, description):
        taking_pic = TakingPicture(attraction=self.get_attraction(id_attraction), description=description)
        taking_pic.save()
        return taking_pic

    def get_settings(self):
        return Settings.objects.last()

    def edit_settings(self, boundaries, logo, loginHours, successAudio, failureAudio):
        raise NotImplementedError("Should have implemented this")

    def create_settings(self, boundaries, loginHours, scoreRules):
        settings = Settings(boundaries=boundaries, loginHours=loginHours, scoreRules=scoreRules)
        settings.save()
        if Settings.objects.all().count() > 1:
            Settings.objects.first().delete()
        return settings

    def edit_info(self, app_name, about_app, how_to_play):
        raise NotImplementedError("Should have implemented this")

    def edit_american_question(self, id_attraction, id_aquestion, question, answers, indexOfCorrectAnswer):
        arr_correct_answers = []
        for ind in indexOfCorrectAnswer:
            index = int(ind) - 1
            arr_correct_answers.append(index)
        aq = self.get_american_question(id_attraction, id_aquestion)
        aq.question = question
        aq.answers = answers
        aq.indexOfCorrectAnswer = indexOfCorrectAnswer
        aq.save()
        return aq



#returns array of names of the media files saved in the media folder
def add_media(media_urls, replace, suffix):
    names_of_files = []
    for file in media_urls:
        file = file.replace('data:' + replace + ';base64,', '')
        #print(file)
        imgdata = base64.b64decode(file)
        filename = str(uuid.uuid4()) + suffix
        with open('media/' + filename, 'wb') as f:
            f.write(imgdata)
        names_of_files += [filename]
    return names_of_files



URL_PREFIX_MEDIA = "http://" + sys.argv[-1] + "/media/"


def addPrefixUrlToSpecificName(name):
    return URL_PREFIX_MEDIA + name


def addPrefixUrl(lst):
    newLst = []
    for name in lst:
        newLst += [addPrefixUrlToSpecificName(name)]
    return newLst


def num_of_media_files():
    path = os.getenv('media')
    print(path)
    num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print(num_files)
    return num_files

