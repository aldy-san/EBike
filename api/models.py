from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=16)
    date_created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username