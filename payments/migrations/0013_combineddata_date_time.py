# Generated by Django 4.2.4 on 2023-08-20 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0012_remove_combineddata_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='combineddata',
            name='date_time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
