from django.contrib import admin
from .models import UserDetails


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'gender', 'created_at')
    ordering = ('-created_at',)