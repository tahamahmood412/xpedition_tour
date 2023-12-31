from django.db import models

# Create your models here.
class fixed_Photo(models.Model):
    name=models.CharField(max_length=100,null=True)
    image=models.FileField(upload_to="images/",max_length=500,null=True)
