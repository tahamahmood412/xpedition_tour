# Generated by Django 4.2.3 on 2023-07-30 21:00

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('special_packages_section', '0002_rename_special_package_name_special_package_package_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='special_package',
            name='details',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
