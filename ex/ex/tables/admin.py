from django.contrib import admin
from .models import Table, ReservationTime, Reservation

admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(ReservationTime)
