# Generated by Django 5.0.4 on 2024-05-11 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobOperation', '0003_jobdata'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdata',
            name='job_giver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.job'),
        ),
    ]
