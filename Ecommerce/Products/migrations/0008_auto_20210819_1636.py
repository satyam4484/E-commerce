# Generated by Django 3.2.6 on 2021-08-19 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0007_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='ProductImage/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='productimg',
        ),
        migrations.AddField(
            model_name='productimage',
            name='Product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Products.product'),
        ),
    ]
