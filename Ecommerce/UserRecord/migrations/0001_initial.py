# Generated by Django 3.2.6 on 2021-08-21 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Products', '0011_subcategory_subimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('mobileno', models.IntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('address', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='UserRecord.useraddress')),
                ('myorder', models.ManyToManyField(to='Products.Product')),
            ],
        ),
    ]
