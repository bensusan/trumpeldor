import sys

from Server.models import *
import null


def addFeedback(question, kind):
    feedback = Feedback(question=question, kind=kind)
    feedback.save()
    return feedback


def addHint(attraction, kind, data, description):
    hint = Hint(attraction=attraction, kind=kind, data=data, description=description)
    hint.save()
    return hint


def addAmericanQuestion(question, answers, indexOfCorrectAnswer, attraction):
    aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer, attraction=attraction)
    aq.save()
    return aq


def addTrack(subTrack, points, length):
    track = None
    if subTrack == null:
        track = Track(length=length)
    else:
        track = Track(subTrack=subTrack, length=length)
    track.save()
    for p in points:
        track.points.add(p)
    return track


def addAttraction(name, x, y, description, picturesURLS, videosURLS, visible):
    attraction = Attraction(name=name, x=x, y=y, description=description, picturesURLS=picturesURLS, videosURLS=videosURLS, visible=visible)
    attraction.save()
    return attraction


def addMessage(title, data):
    message = Message(title=title, data=data)
    message.save()
    return message


def addUser(userName, socialNetwork):
    user = User(name=userName, socialNetwork=socialNetwork)
    user.save()
    return user


def addSlidingPuzzle(attraction, width, height, listOfPicturesNames, description):
    sp = SlidingPuzzle(description=description, attraction=attraction, width=width, height=height, piecesURLS=listOfPicturesNames)
    sp.save()
    return sp


def addPuzzle(attraction, width, height, listOfPicturesNames, description):
    puzzle = Puzzle(description=description, attraction=attraction, width=width, height=height, piecesURLS=listOfPicturesNames)
    puzzle.save()
    return puzzle


def addTakingPicture(attraction, description):
    tp = TakingPicture(description=description, attraction=attraction)
    tp.save()
    return tp


URL_PREFIX_MEDIA = "http://" + sys.argv[-1] + "/media/"


def addPrefixUrlToSpecificName(name):
    return URL_PREFIX_MEDIA + name


def addPrefixUrl(lst):
    newLst = []
    for name in lst:
        newLst += [addPrefixUrlToSpecificName(name)]
    return newLst


def insertDebugData():
    a1 = addAttraction("Meonot dalet", "31.263913", "34.796959", "We Are in Attraction 1", addPrefixUrl(["meonot_dalet_1.jpg", "meonot_dalet_2.jpg"]), [], True)
    a2 = addAttraction("96 building", "31.264934", "34.802062", "We Are in Attraction 2", addPrefixUrl(["96_1.jpg"]), [], True)
    a3 = addAttraction("Shnizale", "31.265129", "34.801575", "We Are in Attraction 3", addPrefixUrl(["shnizale_1.jpg", "shnizale_2.jpg"]), addPrefixUrl(["shnizale_video.mp4"]), True)
    aq1 = addAmericanQuestion("AQ1: Some question here ?", ["Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], [0], a1)
    aq2 = addAmericanQuestion("AQ2: Some question here ?", ["Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], [1], a2)
    aq3 = addAmericanQuestion("AQ3: Some question here ?", ["Incorrect answer",
                                                            "Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer"], [2], a3)

    sp1 = addSlidingPuzzle(a1, 3, 3,addPrefixUrl(["example00.jpeg",
                                                  "example01.jpeg",
                                                  "example02.jpeg",
                                                  "example10.jpeg",
                                                  "example11.jpeg",
                                                  "example12.jpeg",
                                                  "example20.jpeg",
                                                  "example21.jpeg",
                                                  "example22.jpeg"]), "description")

    sp2 = addPuzzle(a2, 3, 3, addPrefixUrl(["example00.jpeg",
                                            "example01.jpeg",
                                            "example02.jpeg",
                                            "example10.jpeg",
                                            "example11.jpeg",
                                            "example12.jpeg",
                                            "example20.jpeg",
                                            "example21.jpeg",
                                            "example22.jpeg"]), "description")

    sp3 = addTakingPicture(a3, "description")

    h11 = addHint(a1, Hint.HINT_TEXT, "This is text hint for Attraction 1", "description")
    h12 = addHint(a1, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("meonot_dalet_1.jpg"), "description")
    h13 = addHint(a1, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"), "description")

    h21 = addHint(a2, Hint.HINT_TEXT, "This is text hint for Attraction 2", "description")
    h22 = addHint(a2, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("96_1.jpg"), "description")
    h23 = addHint(a2, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"), "description")

    h31 = addHint(a3, Hint.HINT_TEXT, "This is text hint for Attraction 3", "description")
    h32 = addHint(a3, Hint.HINT_PICTURE, addPrefixUrlToSpecificName("shnizale_1.jpg"), "description")
    h33 = addHint(a3, Hint.HINT_VIDEO, addPrefixUrlToSpecificName("shnizale_video.mp4"), "description")

    track1 = addTrack(null, [a1], 1)
    track2 = addTrack(null, [a2], 1)
    track3 = addTrack(null, [a3], 1)

    track12 = addTrack(track1, [a2], 2)
    track13 = addTrack(track1, [a3], 2)
    track23 = addTrack(track2, [a3], 2)

    track123 = addTrack(track12, [a3], 3)

    f1 = addFeedback("Feedback 1 rating ?", Feedback.FEEDBACK_RATING)
    f2 = addFeedback("Feedback 2 text ?", Feedback.FEEDBACK_TEXT)

    msg1 = addMessage("Title for message 1", "data for message 1")
    msg2 = addMessage("Title for message 2", "data for message 2")

    anonymousUser = addUser("", "")
    return track123
