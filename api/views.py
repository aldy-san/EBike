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
        return Response({"error" : "yep its eraror"})

class UsersDetailView(APIView):
    def get(self, request, pk):
        user = Users.objects.get(user_id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    def put(self, request, pk):
        data = request.data

        user = Users.objects.get(user_id=pk)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        user = Users.objects.get(user_id=pk)
        user.delete()
        return Response('user telah dihapus')

class StationView(APIView):
    def get(self,request):
        station = Station.objects.all()
        serializer = StationSerializer(station, many=True)
        return Response(serializer.data)
    def post(self, request):
        # request
        station = request.data
        # print(request)
        # Create an user from the above data
        serializer = StationSerializer(data=station, context = {'request':request})
        if serializer.is_valid():
            station_saved = serializer.save()
            return Response({"success": "Station '{}' created successfully".format(station_saved.username)})
        return Response({"error" : "yep its eraror"})

class StationDetailView(APIView):
    def get(self, request, pk):
        station = Station.objects.get(station_id=pk)
        serializer = StationSerializer(station, many=False)
        return Response(serializer.data)
    def put(self, request, pk):
        data = request.data

        station = Station.objects.get(station_id=pk)

        serializer = UserSerializer(station, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        station = Station.objects.get(station_id=pk)
        station.delete()
        return Response('Station telah dihapus')

class CycleView(APIView):
    def get(self,request):
        cycle = Cycle.objects.all()
        serializer = CycleSerializer(cycle, many=True)
        return Response(serializer.data)
    def post(self, request):
        # request
        cycle = request.data
        # print(request)
        # Create an user from the above data
        serializer = StationSerializer(data=cycle, context = {'request':request})
        if serializer.is_valid():
            cycle_saved = serializer.save()
            return Response({"success": "Cycle '{}' created successfully".format(cycle_saved.username)})
        return Response({"error" : "yep its eraror"})

class CycleDetailView(APIView):
    def get(self, request, pk):
        cycle = Station.objects.get(cycle_id=pk)
        serializer = StationSerializer(cycle, many=False)
        return Response(serializer.data)
    def put(self, request, pk):
        data = request.data

        cycle = Cycle.objects.get(cycle_id=pk)

        serializer = UserSerializer(cycle, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        cycle = Cycle.objects.get(cycle_id=pk)
        cycle.delete()
        return Response('Station telah dihapus')

class Login(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.data
            user = Users.objects.filter(username=data['username']).values().first()
            if not user:
                return Response("User tidak ditemukan")

            if data['password'] != user['password']:
                return Response('Password Salah')
            
            payload = {
                'id': user['user_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            return Response({
                'jwt':token
            })
