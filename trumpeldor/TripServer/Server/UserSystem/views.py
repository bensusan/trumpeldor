from rest_framework.response import Response
from django.http import Http404

from rest_framework import generics
from ..serializers import *
from Server.BL.BL import BLProxy
from Server.BL.BL_Implementation import BL_Implementation
from Server.DAL.DAL_Implementation import DAL_Implementation

DAL_Impl = DAL_Implementation()
BL_Impl = BL_Implementation()
BL_Impl.setDAL(DAL_Impl)
BL = BLProxy()
BL.setImplementation(BL_Impl)


class SignUp(generics.GenericAPIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        print("SignUp:", "Got Message data:", request.data, sep="\n")
        user = BL.getUser(request.data)
        if user is None:
            user = BL.createUser(request.data)
        serializer = UserSerializer(user)
        print("Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)


class PreviousTrip(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        print("PreviousTrip:", "Got Message data:", request.data, sep="\n")
        trip = BL.getPreviousUserTrip(request.data)
        serializer = TripSerializer(trip)
        print("Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)


class GetRelevantPreviousTripInformation(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        print("GetRelevantPreviousTripInformation:", "Got Message data:", request.data, sep="\n")
        relevantDataTrip = BL.getRelevantPreviousTripInformation(request.data)
        serializer = GetRelevantPreviousTripInformationSerializer(relevantDataTrip)
        print("Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)


class CreateTrip(generics.GenericAPIView):
    serializer_class = CreateTripSerializer

    def post(self, request, *args, **kwargs):
        print("CreateTrip:", "Got Message data:", request.data, sep="\n")
        trip = BL.createTrip(request.data)
        serializer = TripSerializer(trip)
        print("Sent Message data:", serializer.data, sep="\n")
        return Response(serializer.data)
