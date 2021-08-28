# Generated by Django 3.2.6 on 2021-08-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRecord', '0004_alter_userprofile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Address',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='pincode',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.DeleteModel(
            name='UserAddress',
        ),
    ]