from django.contrib import admin
from .models import company,Companydata,BookData

# Register your models here.


# book data
@admin.register(BookData)
class BookDataAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date', 'price','read','date_time')