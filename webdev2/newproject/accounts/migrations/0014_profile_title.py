# Generated by Django 3.2.7 on 2021-09-11 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_profile_lastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
