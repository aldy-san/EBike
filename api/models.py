from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager

# Create your models here.
class Bikers(AbstractBaseUser, PermissionsMixin):
    user_id = models.BigAutoField(primary_key=True)
    email = models.EmailField(max_length=256, unique=True)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

class Station(models.Model):
    station_id = models.BigAutoField(primary_key=True)
    station_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.station_id)

class Cycle(models.Model):
    cycle_id = models.BigAutoField(primary_key=True)
    cycle_name = models.CharField(max_length=255, default='')
    station_id = models.ForeignKey(Station, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    deskripsi = models.TextField(default='')
    harga = models.IntegerField(default=0)

    def __str__(self):
        return str(self.cycle_id)
