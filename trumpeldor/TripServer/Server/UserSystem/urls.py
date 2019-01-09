from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path('feedback/', views.FeedbackQuestionsList.as_view()),
    path('americanQuestion/<int:pk>/', AmericanQuestion.as_view()),
    # path('hint/<int:pk>/', views.Hint.as_view()),
    path('signUp/', SignUp.as_view()),
    path('previousTrip/', PreviousTrip.as_view()),
    path('GetClass/', GetClass.as_view()),
    # path('x/', X.as_view()),
    # url(r'^getFile/$', FileView.as_view(), name='file-upload'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
