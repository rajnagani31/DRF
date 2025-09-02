from django.db import models

# Create your models here.
class nastahouse(models.Model):
    items = models.CharField(max_length=255)
    datetime = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'nastahouse'