from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

# Create your views here.

class UsersView(APIView):
    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        # request
        user = request.data
        # print(request)
        # Create an user from the above data
        serializer = UserSerializer(data=user, context = {'request':request})
        if serializer.is_valid():
            user_saved = serializer.save()
            return Response({"success": "User '{}' created successfully".format(user_saved.username)})
        return Response({"error" : "yep its error"})