# Generated by Django 4.2.3 on 2023-07-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='booking_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('departure', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('travellers', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=100)),
            ],
        ),
    ]