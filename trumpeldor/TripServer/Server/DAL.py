from Server.models import *
from Server.serializers import *

def getAllTracksWithLength(length):
    return Track.objects.filter(length=length)


# TODO!!!
def getAllAttractions(track):
    pass


# return null or 0 or false  if not exists
def getUser(name, socialNetwork):
    return User.objects.filter(name=name, socialNetwork=socialNetwork)