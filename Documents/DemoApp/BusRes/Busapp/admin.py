from django.contrib import admin
from .models import users,Bus,Reservation,SeatNo

# Register your models here.
admin.site.register(users)
admin.site.register(Bus)
admin.site.register(Reservation)
admin.site.register(SeatNo)
