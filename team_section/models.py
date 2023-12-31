from django.db import models

# Create your models here.
class team_members(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100,null=True)
    image=models.FileField(upload_to="team_members/",max_length=500)
    link=models.CharField(max_length=500,null=True)
