# Generated by Django 3.2.6 on 2021-08-19 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0008_auto_20210819_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to='ProductImage/'),
        ),
    ]
