from django.db import models
from django.contrib.auth.models import AbstractUser

class UserDetails(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    username = models.EmailField(unique=True, null=True)
    email = models.EmailField(max_length=200 , blank=True ,null=True ,unique=True)
    password = models.CharField(max_length=200 , blank=True ,null=True)
    firstname = models.CharField(max_length=100 , blank=True ,null = True)
    lastname = models.CharField(max_length=100 , blank=True ,null = True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['firstname','lastname','username']
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "User Ditails"

# After making changes to the models, run the following commands to apply migrations:
# python manage.py makemigrations
# python manage.py migrate