import null

from ..models import *
from django.http import JsonResponse, HttpResponse

from rest_framework import generics
from ..serializers import *
from .. import BL
from django.core import serializers

#
# class FeedbackQuestionsList(generics.ListCreateAPIView):
#     queryset =Feedback.objects.all()
#     serializer_class = FeedbackSerializer
#
#
# class AmericanQuestion(generics.ListCreateAPIView):
#     queryset = AmericanQuestion.objects.all()
#     serializer_class = AmericanQuestionSerializer
#
#
# class Hint(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hint.objects.all()
#     serializer_class = HintSerializer


class SignUp(generics.CreateAPIView):
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        user = BL.getUser(request.data)
        if(user == None):
            seri = UserSerializer(data=request.data)
            if seri.is_valid():
                seri.save()
                user = BL.getUser(request.data)
            else:
                print("Bug in SignUp method")
        return HttpResponse(serializers.serialize('json', user), content_type='application/json')

class getFile(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        test_file = open('C:/Users/Amit/Desktop/x.jpg', 'rb')
        response = HttpResponse(content=test_file)
        response['Content-Type'] = 'application/jpg'
        response['Content-Disposition'] = 'attachment; filename="%s.jpg"' \
                                      % 'whatever'
        return response











