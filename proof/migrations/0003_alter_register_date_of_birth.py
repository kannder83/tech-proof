# Generated by Django 4.0.4 on 2022-06-04 03:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proof', '0002_register_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]