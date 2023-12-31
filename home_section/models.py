from django.db import models

# Create your models here.
class header_number(models.Model):
    header_number=models.CharField(max_length=50,null=True)

class facebook_link(models.Model):
    facebook_link=models.CharField(max_length=200)

class instagram_link(models.Model):
    instagram_link=models.CharField(max_length=200)

class youtube_link(models.Model):
    youtube_link=models.CharField(max_length=200)
    
class header_heading(models.Model):
    header_heading=models.CharField(max_length=100)

class header_paragraph(models.Model):
    header_paragraph=models.TextField(max_length=500)

class header_logo(models.Model):
    name=models.CharField(max_length=50,null=True)
    header_logo=models.FileField(upload_to="header/",max_length=500)
