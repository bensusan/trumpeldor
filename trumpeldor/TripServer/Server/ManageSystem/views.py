from django.http import JsonResponse, Http404

from rest_framework import generics
from ..serializers import *
from rest_framework.views import APIView


class AmericanQuestion(generics.ListCreateAPIView):     #need to change to Create without list
    queryset = AmericanQuestion.objects.all()
    serializer_class = AmericanQuestionSerializer


class Attraction(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return models.Attraction.objects.get(pk=pk)
        except models.Attraction.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        attr = self.get_object(pk)
        serializer = AttractionSerializer(attr)
        return


    def put(self, request, pk, format=None):
        attr = self.get_object(pk)
        serializer = AttractionSerializer(attr, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)

    # def delete(self, request, pk, format=None):
    #     attr = self.get_object(pk)
    #     attr.delete()
    #     return JsonResponse()
# class Hint(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
#     queryset = Hint.objects.all()
#     serializer_class = HintSerializer


class Feedback(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class SignIn(APIView):

    def get(self, request, format=None):
        return JsonResponse({'name': 'admin', 'password': '1234'})
