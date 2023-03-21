# Generated by Django 4.1.6 on 2023-03-19 11:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_customuser_dateofbirth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationquestiontext',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='applicationquestiontrueorfalse',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='DateofBirth',
            field=models.DateField(default=datetime.datetime(2023, 3, 19, 11, 12, 33, 364000, tzinfo=datetime.timezone.utc)),
        ),
    ]
