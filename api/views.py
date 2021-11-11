from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
import datetime
import jwt

# Create your views here.

# Get all users
class UsersView(APIView):
    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# Get user by user_id
class UserDetailView(APIView):
    def get(self, request, user_id):
        user = Users.objects.get(user_id=user_id)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)

    def put(self, request, user_id):
        data = request.data
        user = Users.objects.get(user_id=user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, user_id):
        user = Users.objects.get(user_id=user_id)
        user.delete()
        return Response('user telah dihapus')

# Registration
class UserRegister(APIView):
    def post(self, request):
        # request
        user = request.data
        # print(request)
        # Create an user from the above data
        serializer = UserSerializer(data=user, context = {'request':request})
        if serializer.is_valid():
            user_saved = serializer.save(password=make_password(user['password']))
            return Response({"success": "User '{}' created successfully".format(user_saved.username)})
        return Response({"error" : "yep its error"})

# Login
class UserLogin(APIView):
    def post(self, request):
        if request.method == 'POST':
            data = request.data
            user = Users.objects.filter(username=data['username']).values().first()
            if not user:
                return Response("User tidak ditemukan")

            # kode di bawah me-return false jika password yang diinput tidak sesuai dengan
            # password yang sudah di-hash
            if not check_password(data['password'], user['password']):
                return Response('Password Salah')
            
            payload = {
                'id': user['user_id'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            return Response({
                'message': "Login Successfully",
                'jwt': token
            })

# Get all station
class StationView(APIView):
    def get(self,request):
        station = Station.objects.all()
        serializer = StationSerializer(station, many=True)
        return Response(serializer.data)

class StationRegister(APIView):
    def post(self, request):
        # request
        station = request.data
        # print(request)
        # Create an user from the above data
        serializer = StationSerializer(data=station, context = {'request':request})
        if serializer.is_valid():
            station_saved = serializer.save()
            return Response({"success": "Station '{}' created successfully".format(station_saved)})
        return Response({"error" : "yep its error"})

# Get station by station id
class StationDetailView(APIView):
    def get(self, request, station_id):
        station = Station.objects.get(station_id=station_id)
        serializer = StationSerializer(station, many=False)
        return Response(serializer.data)

    def put(self, request, station_id):
        data = request.data
        station = Station.objects.get(station_id=station_id)
        serializer = StationSerializer(station, data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response(serializer.data)
        return Response({"error" : "yep its error"})
        
    def delete(self, request, station_id):
        station = Station.objects.get(station_id=station_id)
        station.delete()
        return Response('Station telah dihapus')

# Get all cycle
class CycleView(APIView):
    def get(self,request):
        cycle = Cycle.objects.all()
        serializer = CycleSerializer(cycle, many=True)
        return Response(serializer.data)

class CycleRegistration(APIView):
    def post(self, request):
        # request
        cycle = request.data
        # print(request)
        # Create an user from the above data
        serializer = CycleSerializer(data=cycle, context = {'request':request})
        if serializer.is_valid():
            cycle_saved = serializer.save()
            return Response({"success": "Cycle '{}' created successfully".format(cycle_saved.cycle_id)})
        return Response({"error" : "yep its eraror"})

# Get cycle by cycle_id
class CycleDetailView(APIView):
    def get(self, request, cycle_id):
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        serializer = CycleSerializer(cycle, many=False)
        return Response(serializer.data)

    def put(self, request, cycle_id):
        data = request.data
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        serializer = CycleSerializer(cycle, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, cycle_id):
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        cycle.delete()
        return Response('Cycle telah dihapus')
