from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id','Country','state','air_port_name','pin_code']
    ordering = ['id']


@admin.register(UserTicket)
class UserTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name','last_name','city','from_airport','to_airport']
    ordering=['id']