# Generated by Django 4.2.4 on 2023-08-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0014_combineddata_package_names_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combineddata',
            name='status',
            field=models.CharField(choices=[('verified', 'Verified'), ('not verified', 'Not Verified')], default='Not Verified', max_length=20),
        ),
    ]
