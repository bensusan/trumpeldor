from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from Server.UserSystem import views as usViews
from Server.ManagementSystem import views as msViews
from django.contrib import admin


urlpatterns = [
    path('managementsystem/', include('ManagemnetSystem.urls')),
    path('usersystem/', include('UserSystem.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
