# Generated by Django 3.2.7 on 2021-09-12 04:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_alter_repository_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
    ]