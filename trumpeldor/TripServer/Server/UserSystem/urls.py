from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('signUp/', SignUp.as_view()),
    path('debugHint/', DEBUGHint.as_view()),
    path('previousTrip/', PreviousTrip.as_view()),
    path('getRelevantPreviousTripInformation/', GetRelevantPreviousTripInformation.as_view()),
    path('createTrip/', CreateTrip.as_view()),
    path('getHints/', GetHints.as_view()),
    path('getAmericanQuestion/', GetAmericanQuestion.as_view()),
    path('getFeedbacks/', GetFeedbacks.as_view()),
    path('addToDal/', AddToDal.as_view()),
    path('getExtendedTrack/', GetExtendedTrack.as_view()),
    path('getAttractionForDebug/', GetAttractionForDebug.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
