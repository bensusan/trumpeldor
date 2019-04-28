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
    path('add_medium_path/', views.add_medium_path_page),
    path('add_long_path/', views.add_long_path_page),
    path('add_path/', views.add_path_page),
    path('add_picture/', views.add_picture_page),
    path('add_aq/', views.add_aq_page),
    path('add_aq_edit/', views.add_aq_edit_page),
    path('add_hint_edit/', views.add_hint_edit_page),
    path('add_game_edit/', views.add_game_edit_page),
    path('add_hint/', views.add_hint_page),
    path('pick_hint/', views.pick_hint_page),
    path('edit_hint/', views.edit_hint_page),
    path('edit_hint_edit/', views.edit_hint_edit_page),
    path('pick_aq/', views.pick_aq_page),
    path('pick_aq_edit/', views.pick_aq_edit_page),
    path('pick_hint_edit/', views.pick_hint_edit_page),
    path('pick_path_edit/', views.pick_path_edit_page),
    path('pick_delete_game/', views.pick_delete_game_page),
    path('delete_game/', views.delete_game_page),
    path('pick_path_delete/', views.pick_path_delete_page),
    path('edit_short_path/', views.edit_short_path_page),
    path('edit_medium_path/', views.edit_medium_path_page),
    path('edit_long_path/', views.edit_long_path_page),
    path('feedback/', views.feedback_page),
    path('edit_feedbacks/', views.edit_feedbacks_page),

]

urlpatterns = format_suffix_patterns(urlpatterns)
