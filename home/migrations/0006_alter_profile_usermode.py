# Generated by Django 4.2.4 on 2023-08-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_profile_usermode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='usermode',
            field=models.IntegerField(),
        ),
    ]