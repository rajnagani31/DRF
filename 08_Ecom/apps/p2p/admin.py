from django.contrib import admin

# Register your models here.
from .models import product, User, profile, Blog

admin.site.register(product)
admin.site.register(User)
admin.site.register(profile)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content')