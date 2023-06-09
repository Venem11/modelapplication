# Generated by Django 4.1.6 on 2023-04-03 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_customuser_profileimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='Please type your bio here', max_length=1000),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='profileImage',
            field=models.ImageField(default='ApplyToModelLogo.png', upload_to='profilePic'),
        ),
    ]
