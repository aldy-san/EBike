from django.db.models import manager
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
import datetime
import jwt

# Create your views here.

# Get all users
class UsersView(APIView):
    def get(self,request):
        users = Bikers.objects.all()
        serializer = BikersSerializer(users, many=True)
        return Response({
            "data": serializer.data}, 
            status=200)

# Get user by user_id
class UserDetailView(APIView):
    def get(self, request, user_id):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        user = Bikers.objects.get(user_id=user_id)
        serializer = BikersSerializer(user, many=False)
        return Response({
            "data": serializer.data},
            status=200)
        # return 404 kalau user tidak ada

    def put(self, request, user_id):
        data = request.data
        # permission_classes = [IsAuthenticated | IsAdminUser]
        user = Bikers.objects.get(user_id=user_id)
        serializer = BikersSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({
            "data": serializer.data},
            status=200)
        # return 404 kalau user tidak ada

    def delete(self, request, user_id):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        user = Bikers.objects.get(user_id=user_id)
        user.delete()
        return Response({
            "message": 'User {} telah dihapus'.format(user['user_id'])},
            status=200)
        # return 404 kalau user tidak ada

# Registration
class UserRegister(APIView):
    def post(self, request):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        user = request.data
        serializer = BikersSerializer(data=user, context = {'request':request})
        if serializer.is_valid():
            serializer.save(password=make_password(user['password']))
            return Response({
                "message" : "User has been created succesfully"
            },
                status=200)
        return Response({
            "error" : "An error encountered"},
            status=406)
        # return 404 kalau user tidak ada

# Login
class UserLogin(APIView):
    def post(self, request):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        data = request.data
        user = Bikers.objects.filter(username=data['username']).values().first()
        if not user:
            return Response({"User tidak ditemukan"}, status=401)

        # kode di bawah me-return false jika password yang diinput tidak sesuai dengan
        # password yang sudah di-hash
        if not check_password(data['password'], user['password']):
            return Response({'Password Salah'}, status=401)
            
            # exp = expired, iat = issued at
        payload = {
            'id': user['user_id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
            'iat': datetime.datetime.utcnow()
        }

        # token = RefreshToken.for_user(user)
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            "status": HttpResponse.status_code,
            'jwt': token
        }
        return response
        # return 404 kalau user tidak ada

# User authentication
class UserAuthentication(APIView):
    def get(self, request):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed({"Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed({"Unauthenticated"}, status=401)

        user = Bikers.objects.filter(user_id=payload['id']).first()
        serializer = BikersSerializer(user)

        return Response({
            "data": serializer.data},
            status=200)

# Logout
class UserLogout(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            "Message": "User has logout successfully"
        }
        return response

# Get all station
class StationView(APIView):
    def get(self,request):
        station = Station.objects.all()
        serializer = StationSerializer(station, many=True)
        return Response(serializer.data)

class StationRegister(APIView):
    # permission_classes = [IsAdminUser]
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
    # permission_classes = [IsAuthenticated | IsAdminUser]
    def get(self, request, station_id):
        station = Station.objects.get(station_id=station_id)
        serializer = StationSerializer(station, many=False)
        return Response(serializer.data)

    def put(self, request, station_id):
        # permission_classes = [IsAdminUser]
        data = request.data
        station = Station.objects.get(station_id=station_id)
        serializer = StationSerializer(station, data=request.data)
        if serializer.is_valid():
            saved_data = serializer.save()
            return Response(serializer.data)
        return Response({"error" : "yep its error"})
        
    def delete(self, request, station_id):
        # permission_classes = [IsAdminUser]
        station = Station.objects.get(station_id=station_id)
        station.delete()
        return Response('Station telah dihapus')

# Get all cycle
class CycleView(APIView):
    def get(self,request):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        cycle = Cycle.objects.all()
        serializer = CycleSerializer(cycle, many=True)
        return Response(serializer.data)

class CycleRegistration(APIView):
    def post(self, request):
        # permission_classes = [IsAdminUser]
        cycle = request.data
        serializer = CycleSerializer(data=cycle, context = {'request':request})
        if serializer.is_valid():
            cycle_saved = serializer.save()
            return Response({"success": "Cycle '{}' created successfully".format(cycle_saved.cycle_id)})
        return Response({"error" : "yep its eraror"})

# Get cycle by cycle_id
class CycleDetailView(APIView):
    def get(self, request, cycle_id):
        # permission_classes = [IsAuthenticated | IsAdminUser]
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        serializer = CycleSerializer(cycle, many=False)
        return Response(serializer.data)

    def put(self, request, cycle_id):
        # permission_classes = [IsAdminUser]
        data = request.data
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        serializer = CycleSerializer(cycle, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, cycle_id):
        # permission_classes = [IsAdminUser]
        cycle = Cycle.objects.get(cycle_id=cycle_id)
        cycle.delete()
        return Response('Cycle telah dihapus')
