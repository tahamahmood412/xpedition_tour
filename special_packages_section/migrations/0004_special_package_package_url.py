# Generated by Django 4.2.4 on 2023-08-07 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('special_packages_section', '0003_special_package_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_package',
            name='package_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
