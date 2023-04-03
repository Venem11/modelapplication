# Generated by Django 4.1.6 on 2023-04-03 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_customuser_bio_alter_customuser_profileimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(default='Please enter a title for your event', max_length=30)),
                ('EventDetails', models.CharField(default='Please enter a description for your event', max_length=600)),
                ('EventStartDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('EventEndDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
