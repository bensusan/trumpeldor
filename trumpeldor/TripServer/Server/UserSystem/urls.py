from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # path('feedback/', views.FeedbackQuestionsList.as_view()),
    path('americanQuestion/<int:pk>/', views.AmericanQuestion.as_view()),
    # path('hint/<int:pk>/', views.Hint.as_view()),
    path('signUp/', views.SignUp.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
