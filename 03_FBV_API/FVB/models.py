from django.db import models

# Create your models here.
class Country(models.Model):
    Country = models.CharField(max_length = 100 , blank= False , null= False)
    state = models.CharField(max_length = 100 , blank= False , null= False)
    air_port_name = models.CharField(max_length=100 , blank=False , null=False)
    pin_code =  models.IntegerField(blank= True )

    def __str__(self):
        return f"{self.Country} - {self.state} - {self.air_port_name}"

    # def __str__(self):
    #     return self.state

    class Meta:
        db_table = 'Country'



class UserTicket(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100 , blank=False ,null=False)
    last_name = models.CharField(max_length=100  , blank=False ,null=False)
    city = models.CharField(max_length=100  , blank=False ,null=False)
    from_airport = models.ForeignKey(Country,max_length=100,blank=False ,null = False ,on_delete=models.DO_NOTHING ,related_name='from_airport')
    to_airport = models.ForeignKey(Country , max_length=100 ,blank=False, null= False ,on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'UserTicket'



class Courese(models.Model):
    name = models.CharField(max_length=100 , blank=False ,null=False)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100 , blank=False ,null=False)
    roll= models.IntegerField(unique=True)
    course = models.ManyToManyField("Courese")


####### 1NF 
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    def __str__(self):
        return self.customer_name
    
class Product(models.Model):
    order = models.ForeignKey(Order, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100 ,null= True)
