from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('signIn/', views.sign_in_page),
    path('attractions/', views.manage_attractions_page),
]

urlpatterns = format_suffix_patterns(urlpatterns)
