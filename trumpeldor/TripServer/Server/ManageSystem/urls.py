from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.views.generic.base import TemplateView

from django.contrib import admin
from . import views

urlpatterns = {
    path('attraction/<int:id_attr>/hint/<int:id_hint>/', Hint.as_view()),
    path('attraction/<int:id_attr>/hint/', HintsList.as_view()),
    path('attraction/<int:id_attr>/aquestion/<int:id_quest>/', AmericanQuestion.as_view()),
    path('attraction/<int:id_attr>/aquestion/', AmericanQuestionsList.as_view()),
    path('feedback/', FeedbackList.as_view()),
    path('feedback/<int:id>/', Feedback.as_view()),  #works get and delete, there is no put
    path('attraction/', AttractionsList.as_view()),
    path('attraction/<int:id>/', Attraction.as_view()),
    path('track/', TracksList.as_view()),
    path('track/<int:id>/', Track.as_view()),
    path('track/<int:id>/<action>', Track.as_view()),
    path('info/', Info.as_view()),
    path('attraction/<int:id_attr>/sliding_puzzle/', SlidingPuzzleList.as_view()),
    path('attraction/<int:id_attr>/puzzle/', PuzzleList.as_view()),
    #path('attraction/<int:id_attr>/find_the_differences/', FindTheDifferencesList.as_view()),  #not relevant
    path('attraction/<int:id_attr>/taking_pic/', TakingPictureList.as_view()),
    path('settings/', SettingsList.as_view()),

}

urlpatterns = format_suffix_patterns(urlpatterns)
