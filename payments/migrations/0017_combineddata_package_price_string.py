# Generated by Django 4.2.4 on 2023-08-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0016_alter_combineddata_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='combineddata',
            name='package_price_string',
            field=models.CharField(max_length=100, null=True),
        ),
    ]