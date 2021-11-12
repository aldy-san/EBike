from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=16)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.username)

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
