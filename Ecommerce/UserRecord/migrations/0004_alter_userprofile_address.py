# Generated by Django 3.2.6 on 2021-08-21 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserRecord', '0003_alter_userprofile_mobileno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserRecord.useraddress'),
        ),
    ]
