# Generated by Django 4.2.3 on 2023-07-26 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer_section', '0003_rename_image_footer_logo_footer_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer_gmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_gmail', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='footer_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_location', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='footer_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_number', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='footer_paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_paragraph', models.TextField(max_length=300, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='footer_logo',
            name='footer_gmail',
        ),
        migrations.RemoveField(
            model_name='footer_logo',
            name='footer_location',
        ),
        migrations.RemoveField(
            model_name='footer_logo',
            name='footer_number',
        ),
        migrations.RemoveField(
            model_name='footer_logo',
            name='footer_paragraph',
        ),
    ]
