from gc import is_finalized
from pyexpat import model

from django.db import models

# Create your models here.
class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, default="")

    def __str__(self):
        return self.user.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Email(models.Model):
    email = models.EmailField()
    is_sended = models.BooleanField(default=False)  
    is_fialed = models.Aggregate(models.BooleanField(default=False))

    def __str__(self):
        return self.email