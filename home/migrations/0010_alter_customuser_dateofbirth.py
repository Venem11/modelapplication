# Generated by Django 4.1.6 on 2023-03-19 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_remove_applicationquestiontrueorfalse_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DateofBirth',
            field=models.DateField(default=datetime.datetime(2023, 3, 19, 11, 3, 59, 77925, tzinfo=datetime.timezone.utc)),
        ),
    ]
