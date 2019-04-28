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
    path('feedback/<int:id>/', Feedback.as_view()),
    path('attraction/', AttractionsList.as_view()),
    path('attraction/<int:id>/', Attraction.as_view()),
    path('track/', TracksList.as_view()),
    path('track/<int:id>/', Track.as_view()),
    path('track/<int:id>/<action>', Track.as_view()),
    path('info/', Info.as_view()),
    path('info/<int:id>/', InfoSpecific.as_view()),
    path('attraction/<int:id_attr>/sliding_puzzle/', SlidingPuzzleList.as_view()),
    path('attraction/<int:id_attr>/puzzle/', PuzzleList.as_view()),
    path('attraction/<int:id_attr>/find_the_differences/', FindTheDifferencesList.as_view()),
    # path('entertainment/', EntertainmentsList.as_view()),
    # path('americanQuestion/', views.AmericanQuestion.as_view()),
    # path('attraction/(\d+)/(\d+)/', views.SpecificAttraction.as_view()),
    # path('attractions/', views.Attractions.as_view()),
    # path('tracks/', views.Tracks.as_view()),
    # path('feedback/', views.Feedback.as_view()),
    # # path('hint/', views.Hint.as_view()),
    # path('signin/', views.SignIn.as_view()),
    # path('main/', views.main_page, name='home'),
    # url('map/$', views.map_page, name='home'),
    # url('maptrack/$', views.map_track_page, name='map-track'),
    # url('addattraction/$', views.add_attraction_page, name='add-attraction'),
    # url('americanquestion/$', views.add_AQ_page, name='add-aq'),
    # url('attractionexist/(\d+)/(\d+)/$', views.checkIfPointExist),
    # # path('main/deleteattraction/', views.delete_attraction, name='delete-attraction'),
    # # path('main/editattraction/', views.edit_attraction, name='edit-attraction'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
