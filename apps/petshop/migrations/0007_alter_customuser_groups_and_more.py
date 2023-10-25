# Generated by Django 4.2.2 on 2023-06-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('petshop', '0006_remove_customuser_apellido_remove_customuser_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_groups', related_query_name='custom_user_group', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_permissions', related_query_name='custom_user_permission', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
