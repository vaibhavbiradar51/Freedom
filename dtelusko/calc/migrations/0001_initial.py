# Generated by Django 2.2 on 2020-01-27 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idNumber', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
