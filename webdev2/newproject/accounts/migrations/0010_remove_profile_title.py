# Generated by Django 3.2.7 on 2021-09-11 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_profile_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]