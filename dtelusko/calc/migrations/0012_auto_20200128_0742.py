# Generated by Django 2.2 on 2020-01-28 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_auto_20200128_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 28, 7, 42, 31, 116099)),
        ),
    ]