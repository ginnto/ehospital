# Generated by Django 4.1.7 on 2024-06-24 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctors',
            name='department',
        ),
    ]
