# Generated by Django 3.2.6 on 2021-08-23 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserRecord', '0009_delete_useraddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='state',
        ),
    ]
