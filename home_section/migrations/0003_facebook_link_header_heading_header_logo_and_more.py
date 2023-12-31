# Generated by Django 4.2.3 on 2023-07-26 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_section', '0002_alter_home_header_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='facebook_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='header_heading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_heading', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='header_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_logo', models.FileField(max_length=500, upload_to='header/')),
            ],
        ),
        migrations.CreateModel(
            name='header_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_number', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='header_paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_paragraph', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='instagram_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='youtube_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='home',
        ),
    ]
