from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class all_package(models.Model):
    package_url=models.CharField(max_length=100,null=True)
    package_name=models.CharField(max_length=100,null=True)
    image=models.FileField(upload_to="all_packages/",max_length=500,null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    price=models.CharField(max_length=100,null=True)
    details=HTMLField(null=True)