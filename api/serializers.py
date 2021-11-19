from django.db import models
from rest_framework import serializers
from .models import *

class BikersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bikers
        fields = [
            'email',
            'password',
        ]

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = [
            'station_id',
            'station_name',
        ]

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = [
            'cycle_id',
            'cycle_name',
            'station_id',
            'status',
            'deskripsi',
            'harga',
        ]

# class UserSerializer(serializers.Serializer):
#     # user_id = serializers.BigAutoField(primary_key=True)
#     username = serializers.CharField(max_length=256)
#     email = serializers.CharField(max_length=256)
#     password = serializers.CharField(max_length=120)
#     # date_created = serializers.DateField(auto_now_add=True)