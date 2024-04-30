from rest_framework import serializers
from . import models

class ReservationsSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = models.Reservations
        fields = '__all__'