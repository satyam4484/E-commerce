# Generated by Django 3.2.6 on 2021-08-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRecord', '0002_auto_20210821_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='mobileno',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
