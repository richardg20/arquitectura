# Generated by Django 4.2.6 on 2023-10-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0012_userprofile_remove_producto_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='altura',
            field=models.EmailField(max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='edad',
            field=models.EmailField(max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='objetivo',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='peso',
            field=models.EmailField(max_length=3),
        ),
    ]
