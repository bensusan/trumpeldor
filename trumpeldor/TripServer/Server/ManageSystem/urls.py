from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib import admin
from . import views

urlpatterns = [
    path('americanQuestion/', views.AmericanQuestion.as_view()),
    path('attraction/<int:pk>/', views.Attraction.as_view()),
    path('feedback/', views.Feedback.as_view()),
    #path('hint/', views.Hint.as_view()),
    path('signin/', views.SignIn.as_view()),
    url(r'^admin/', admin.site.urls),

]

urlpatterns = format_suffix_patterns(urlpatterns)
