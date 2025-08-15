from django.db import models

import datetime

# Create your models here.
class company(models.Model):
    id = models.BigAutoField(primary_key=True)
    company_name= models.CharField(max_length=255)
    is_active=models.BooleanField(null=True)

    class Meta:
        db_table = "company"
        verbose_name = "Company"
        ordering = ['id']

class Companydata(models.Model):
    company = models.ForeignKey(company, on_delete=models.CASCADE)
    current_working_project = models.IntegerField()
    total_team= models.IntegerField()
    team_manager= models.CharField(max_length=255)

    class Meta:
        db_table = "company_data"
                          
class BookData(models.Model):
    title = models.CharField(max_length=200 ,blank=True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField(default=datetime.date.today)
    read = models.CharField(auto_created=True,null=True ,max_length=100 )
    date_time= models.DateTimeField("Date Time" , auto_now=False,auto_now_add=True ,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    
    def __str__(self):
        return self.title      

    class Meta:
        db_table = "Book Data"