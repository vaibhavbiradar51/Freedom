# Generated by Django 2.2 on 2020-01-27 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0005_auto_20200127_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 27, 23, 59, 53, 352408)),
        ),
    ]
