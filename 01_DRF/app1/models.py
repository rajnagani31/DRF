from django.db import models

# Create your models here.
choice = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]
class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=choice)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user details"
        verbose_name = "User data"
        verbose_name_plural = "User data"
        ordering = ['id']