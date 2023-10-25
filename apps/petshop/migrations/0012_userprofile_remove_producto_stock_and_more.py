# Generated by Django 4.2.6 on 2023-10-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petshop', '0011_rename_contraseña_user_usuario_contraseña_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.EmailField(max_length=254)),
                ('peso', models.EmailField(max_length=254)),
                ('altura', models.EmailField(max_length=254)),
                ('objetivo', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
        migrations.AddField(
            model_name='usuario',
            name='rutina_completa',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='producto',
            name='sku',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]