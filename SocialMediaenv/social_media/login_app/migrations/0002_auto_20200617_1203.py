# Generated by Django 3.0.7 on 2020-06-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilepic',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]
