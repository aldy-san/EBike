
from django.urls import path

from .views import *


app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/register/', Register.as_view()),
    path('users/login/', Login.as_view()),
]