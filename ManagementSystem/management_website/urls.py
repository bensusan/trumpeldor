from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('signIn/', views.sign_in_page),
    path('attractions/', views.manage_attractions_page, name='attractions'),
    path('add_attraction/', views.add_attraction_page, name='add_attraction'),
    path('edit_attraction/', views.edit_attraction_page, name='edit_attraction'),
    path('main/', views.main_page),
    path('add_game/', views.add_game_page),
    path('additional_info/', views.info_page),
    path('add_short_path/', views.add_short_path_page),
]

urlpatterns = format_suffix_patterns(urlpatterns)
