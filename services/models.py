from django.db import models

# Create your models here.
class Customer(models.Model):
    c_name = models.CharField(max_length=30)
    c_address = models.CharField(max_length=50)
    c_email = models.EmailField()
    phone = models.IntegerField()
    def __str__(self):
        return self.c_name
    
class Services(models.Model):
 providing_services = models.CharField(max_length=50)
 sp_name = models.CharField(max_length=50) 
 
 service_benifits = models.CharField(max_length=100)
 sp_phone = models.CharField(max_length=50)
 def __str__(self):
        return self.providing_services
 
 
class Appointment(models.Model):
 a_date = models.DateField()
 a_time=models.CharField(max_length=50)
 a_cost=models.IntegerField()
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 services = models.ForeignKey(Services, on_delete=models.CASCADE)
 
