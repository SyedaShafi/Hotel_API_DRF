from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.
class HotelViewset(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializer_class = serializers.HotelSerializer


class ReviewViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer