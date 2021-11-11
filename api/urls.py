
from django.urls import path

from .views import *


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UsersView.as_view()),
    path('user/detail/<int:user_id>', UserDetailView.as_view()),
    path('user/register/', UserRegister.as_view()),
    path('user/login/', UserLogin.as_view()),
    path('stations/', StationView.as_view()),
    path('station/register/', StationRegister.as_view()),
    path('station/detail/<int:station_id>', StationDetailView.as_view()),
    path('cycles/', CycleView.as_view()),
    path('cycle/register/', CycleRegistration.as_view()),
    path('cycle/detail/<int:cycle_id>', CycleDetailView.as_view())
]