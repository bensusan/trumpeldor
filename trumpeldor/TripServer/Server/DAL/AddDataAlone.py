import null

from Server.models import *


def addFeedback(question, kind):
    feedback = Feedback(question=question, kind=kind)
    feedback.save()
    return feedback


def addHint(attraction, kind, data):
    hint = Hint(attraction=attraction, kind=kind, data=data)
    hint.save()
    return hint


def addAmericanQuestion(question, answers, indexOfCorrectAnswer, attraction):
    aq = AmericanQuestion(question=question, answers=answers, indexOfCorrectAnswer=indexOfCorrectAnswer, attraction=attraction)
    aq.save()
    return aq


def addTrack(subTrack, points, length):
    track = Track(subTrack=subTrack, length=length)
    track.save()
    track.points.add(points)
    return track


def addAttraction(name, x, y, description, picturesURLS, videosURLS):
    attraction = Attraction(name=name, x=x, y=y, description=description, picturesURLS=picturesURLS, videosURLS=videosURLS)
    attraction.save()
    return attraction


def main():
    a1 = addAttraction("Attraction 1", "0.1", "0.1", "We Are in Attraction 1", "x.jpg", "")
    a2 = addAttraction("Attraction 2", "0.2", "0.2", "We Are in Attraction 2", "y.png", "")
    aq1 = addAmericanQuestion("AQ1: Some question here ?", ["Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 1, a1)
    aq2 = addAmericanQuestion("AQ2: Some question here ?", ["Incorrect answer",
                                                            "Correct answer",
                                                            "Incorrect answer",
                                                            "Incorrect answer"], 2, a2)
    h11 = addHint(a1, Hint.HINT_TEXT, "This is text hint for Attraction 1")
    h12 = addHint(a1, Hint.HINT_PICTURE, "x.jpg")
    h13 = addHint(a1, Hint.HINT_MAP, "0.1,0.1")

    h21 = addHint(a2, Hint.HINT_PICTURE, "y.png")
    h22 = addHint(a2, Hint.HINT_TEXT, "This is text hint for Attraction 2")
    h23 = addHint(a2, Hint.HINT_MAP, "0.2,0.2")

    track1 = addTrack(null, [a1], 1)
    track2 = addTrack(null, [a2], 1)

    track12 = addTrack(track1, [a2], 2)

    f1 = addFeedback("Feedback 1 rating ??", Feedback.FEEDBACK_RATING)
    f2 = addFeedback("Feedback 2 text ??", Feedback.FEEDBACK_TEXT)



# if __name__ == "__main__":
#     main()