from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly 
from . import models
from . import serializers
# Create your views here.
class ReservationsViewset(viewsets.ModelViewSet):
    queryset = models.Reservations.objects.all()
    serializer_class = serializers.ReservationsSerializer