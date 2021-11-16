from django.db import models
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return {
            "username": user.username,
            "email": user.email
        }

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