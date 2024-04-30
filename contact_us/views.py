from django.shortcuts import render
from rest_framework import viewsets
from . models import ContactUs
from . serializers import ContactUsSerializers
# Create your views here.

class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializers