from django.db import models



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
                          