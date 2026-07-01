from django.contrib import admin
from .models import  Rooms,reservation,RoomImage
# Register your models here.


admin.site.register( Rooms)
admin.site.register(reservation)
admin.site.register(RoomImage)