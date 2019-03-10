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
    path('main/', views.main_page),
    # path('short_path/', views.short_path),
    # path('medium_path/', views.medium_path),
    # path('long_path/', views.long_path),
]

urlpatterns = format_suffix_patterns(urlpatterns)
