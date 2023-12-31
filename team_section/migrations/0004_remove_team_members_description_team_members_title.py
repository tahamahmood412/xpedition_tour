# Generated by Django 4.2.3 on 2023-07-26 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_section', '0003_team_members_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team_members',
            name='description',
        ),
        migrations.AddField(
            model_name='team_members',
            name='title',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
