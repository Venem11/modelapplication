# Generated by Django 4.1.6 on 2023-03-19 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_customuser_dateofbirth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='DateofBirth',
            field=models.DateField(default=datetime.datetime(2023, 3, 19, 11, 8, 48, 773713, tzinfo=datetime.timezone.utc)),
        ),
    ]
