# Generated by Django 3.2.6 on 2021-08-23 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0014_auto_20210822_1239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='Address',
            new_name='address',
        ),
    ]
