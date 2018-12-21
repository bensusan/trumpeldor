from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .ManageSystem import urls

urlpatterns = [
    path('managementsystem/', include('ManageSystem.urls')),
    path('usersystem/', include('UserSystem.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
