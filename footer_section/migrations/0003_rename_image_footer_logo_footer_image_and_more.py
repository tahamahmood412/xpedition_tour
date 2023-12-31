# Generated by Django 4.2.3 on 2023-07-25 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footer_section', '0002_footer_logo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footer_logo',
            old_name='image',
            new_name='footer_image',
        ),
        migrations.AddField(
            model_name='footer_logo',
            name='footer_gmail',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='footer_logo',
            name='footer_location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='footer_logo',
            name='footer_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='footer_logo',
            name='footer_paragraph',
            field=models.TextField(max_length=300, null=True),
        ),
    ]