# Generated by Django 3.2.6 on 2021-08-19 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat', models.CharField(max_length=200)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductPrice', models.IntegerField()),
                ('ProductDesc', models.CharField(max_length=2000)),
                ('slug', models.SlugField(unique=True)),
                ('ProductCat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.subcategory')),
            ],
        ),
    ]