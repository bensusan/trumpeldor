from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.views.generic.base import TemplateView

from django.contrib import admin
from . import views

urlpatterns = {
    path('hint/', Hint.as_view()),
    path('aquestion/', AmericanQuestion.as_view()),
    path('feedback/', Feedback.as_view()),
    path('attraction/', AttractionsList.as_view()),
    path('attraction/<int:id>/', Attraction.as_view()),
    path('track/', Track.as_view()),
<<<<<<< HEAD
    path('signin/', views.sign_in_page),
    path('attractions/', views.manage_attractions_page),
=======
    # path('americanQuestion/', views.AmericanQuestion.as_view()),
    # path('attraction/(\d+)/(\d+)/', views.SpecificAttraction.as_view()),
    #path('attractions/', views.Attractions.as_view()),
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
