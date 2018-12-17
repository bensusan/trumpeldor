import null

from ..models import *
from django.http import JsonResponse

from rest_framework import generics
from ..serializers import *
from .. import BL



class FeedbackQuestionsList(generics.ListCreateAPIView):
    queryset =Feedback.objects.all()
    serializer_class = FeedbackSerializer


class AmericanQuestion(generics.ListCreateAPIView):
    queryset = AmericanQuestion.objects.all()
    serializer_class = AmericanQuestionSerializer


class Hint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hint.objects.all()
    serializer_class = HintSerializer


class SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        lastSeen = null
        if BL.checkIfExists(request.data):
            lastSeen = request.data.lastSeen
        else:
            self.serializer_class.save(user=request.user)
        return JsonResponse({'lastSeen': lastSeen})








