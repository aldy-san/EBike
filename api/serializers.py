from django.db import models
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            'user_id',
            'username',
            'email',
            'password',
            'date_created',
        ]
# class UserSerializer(serializers.Serializer):
#     # user_id = serializers.BigAutoField(primary_key=True)
#     username = serializers.CharField(max_length=256)
#     email = serializers.CharField(max_length=256)
#     password = serializers.CharField(max_length=120)
#     # date_created = serializers.DateField(auto_now_add=True)