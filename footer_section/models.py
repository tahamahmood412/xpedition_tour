from django.db import models

# Create your models here.
class footer_logo(models.Model):
    name=models.CharField(max_length=50,null=True)
    footer_image=models.FileField(upload_to="footer/",max_length=500,null=True)

class footer_paragraph(models.Model):
    footer_paragraph=models.TextField(max_length=300,null=True)

class footer_number(models.Model):
    footer_number=models.CharField(max_length=50,null=True)


class footer_gmail(models.Model):
    footer_gmail=models.CharField(max_length=50,null=True)

    
class footer_location(models.Model):
    footer_location=models.CharField(max_length=50,null=True)

class developer(models.Model):
    developer_name=models.CharField(max_length=50,null=True)
    developer_link=models.CharField(max_length=50,null=True)

class youtube_url(models.Model):
    name=models.CharField(max_length=50,null=True)
    url=models.CharField(max_length=50,null=True)
