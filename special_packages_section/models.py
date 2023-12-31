from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class special_package(models.Model):
    package_url=models.CharField(max_length=100,null=True)
    package_name=models.CharField(max_length=100,null=True)
    image=models.FileField(upload_to="special_packages/",max_length=500,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    days_nights = models.CharField(max_length=100)
    max_people = models.CharField(max_length=100)
    location=models.CharField(max_length=100,null=True)
    reviews=models.CharField(max_length=100,null=True)
    price=models.CharField(max_length=100,null=True)
    details=details=HTMLField(null=True)
 