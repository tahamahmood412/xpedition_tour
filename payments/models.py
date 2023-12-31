from django.db import models
from django.contrib import admin

class CombinedData(models.Model):
    PAID_CHOICES = (
        ('verified', 'Verified'),
        ('not verified', 'Not Verified'),
    )
    phone=models.CharField(max_length=100,null=True)
    package_names_string = models.CharField(max_length=100,null=True)
    package_price_string =models.CharField(max_length=100,null=True)
    full_name = models.CharField(max_length=100)
    no_of_travellers = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100,null=True)
    nationality = models.CharField(max_length=100,null=True)
    account_name = models.CharField(max_length=100)
    date_time = models.CharField(max_length=100,null=True)
    # date_time = models.DateTimeField(null=True)
    account_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to="payments/", null=True)
    # status = models.CharField(max_length=20, choices=PAID_CHOICES, null=True)
    status = models.CharField(max_length=20, choices=PAID_CHOICES, default='not verified')

    
   

