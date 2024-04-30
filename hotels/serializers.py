from rest_framework import serializers
from . import models

class HotelSerializer(serializers.ModelSerializer):
   class Meta:
        model = models.Hotel
        fields = '__all__'
       

class ReviewSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Review
        fields = '__all__'