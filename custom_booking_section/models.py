from django.db import models

# Create your models here.
class booking_data(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    travellers = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount=models.CharField(max_length=100,null=True)
 
class departure_city(models.Model):
    departure_city=models.CharField(max_length=100)

class destination_city(models.Model):
    destination_city=models.CharField(max_length=100)