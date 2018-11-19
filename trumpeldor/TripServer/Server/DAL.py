from polls.models import *


def getAllTracksWithLength(length):
    return Track.objects.filter(length=length)


# TODO!!!
def getAllAttractions(track):
    pass
