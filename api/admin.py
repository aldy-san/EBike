from django.contrib import admin
from .models import *

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_created',)

class StationsAdmin(admin.ModelAdmin):
    list_display = ('station_name',)

class CyclesAdmin(admin.ModelAdmin):
    list_display = ('cycle_id',)  

admin.site.register(Users, UsersAdmin)
admin.site.register(Station, StationsAdmin)
admin.site.register(Cycle, CyclesAdmin)
