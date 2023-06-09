# Generated by Django 4.1.6 on 2023-03-19 10:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_customuser_pornname_alter_customuser_dateofbirth'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationquestiontext',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicationquestiontrueorfalse',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='DateofBirth',
            field=models.DateField(default=datetime.datetime(2023, 3, 19, 10, 58, 20, 617523, tzinfo=datetime.timezone.utc)),
        ),
    ]
