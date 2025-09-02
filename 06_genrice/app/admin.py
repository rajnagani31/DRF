from django.contrib import admin
from .models import nastahouse  


@admin.register(nastahouse)
class NastahouseAdmin(admin.ModelAdmin):    
    list_display = ('id', 'items', 'datetime', 'is_active', 'price')  
    list_filter = ('is_active', 'datetime')  
    search_fields = ('items',)  
