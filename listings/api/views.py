from django.shortcuts import render
from rest_framework import generics
from .models import House
from .serializers import HouseSerializer


# GET, POST
class HouseList(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


# GET, DELETE, PUT
class HouseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
