from django.contrib import admin
from .models import *

# Register your models here.
class BikersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'email', 'date_created',)

class StationsAdmin(admin.ModelAdmin):
    list_display = ('station_name',)

class CyclesAdmin(admin.ModelAdmin):
    list_display = ('cycle_id',)  

admin.site.register(Bikers, BikersAdmin)
admin.site.register(Station, StationsAdmin)
admin.site.register(Cycle, CyclesAdmin)
