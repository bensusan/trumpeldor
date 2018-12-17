from Server import DAL


# /////////////////////////////////////////////////////////
#                    Functions for BL
# /////////////////////////////////////////////////////////


# need to think if we want hamilton, also need to consider that we need to take the shortest VALID route from point
# to point. we want route that will be easy to walk in it.
# startPoint - {'x': _, 'y': _}
# points - [{'idNumber': _, 'x': _, 'y': _}, ...]
# will return the order which need to visit. Also will tell the length of the track.
# TODO
def _calculateThePath(startPoint, points):
    pass


# TODO
# get track and order which the points has to be to the current user. also get the length of the track.
# return the track with the relevant information to send to the PL.
# should return {'track': _, 'length' _}
def _getTheRelevantInformationAboutTrack(track, pointsOrderAndLength):
    pass


# location - {'x': _, 'y': _ }
# get the track and the location of the user.
# find the order of the points in track according to location
# return the track and the total length of it
# should return {'track': _, 'length' _}
def _calculateTrack(location, track):
    # will be list from the shape: [{'idNumber': _, 'x': _, 'y': _},...]
    points = DAL.getAllAttractionsLocations(track)
    pointsOrderAndLength = _calculateThePath(location, points)
    trackAfterWithLength = _getTheRelevantInformationAboutTrack(track, pointsOrderAndLength)
    return trackAfterWithLength


# assume there are tracks.
# location - presents the location of the user. It is an object with 2 fields: {x: _ , y: _}
# tracks - tracks which need to pass over them.
# the function will pass over the tracks to sort them by the user location and choose the shortest track
def _searchForTheShortestTrack(location, tracks):
    chosenTrackWithLength = {'track': {}, 'length': float("inf")}
    for track in tracks:
        trackSortedWithLength = _calculateTrack(location, track)
        if trackSortedWithLength.length < chosenTrackWithLength.length:
            chosenTrackWithLength = trackSortedWithLength

    return chosenTrackWithLength


# location - presents the location of the user. It is an object with 2 fields: {x: _ , y: _}
# length - presents how long user wants his track to be. (short, medium, long)
# the function will search from all the tracks that satisfies length, the shortest track according to user's location.
def sendTrack(location, length):
    tracks = DAL.getAllTracksWithLength(length)
    chosenTrack = _searchForTheShortestTrack(location, tracks)
    return chosenTrack


def checkIfExists(user):
    return DAL.getUser(user.name, user.socialNetwork)
