from django.shortcuts import render
from rest_framework import generics
from .models import Hotels
from .serializers import HotelSerializer

class hotel_view(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer

