# Generated by Django 3.0.3 on 2020-02-26 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200225_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_image/%d/%m/%Y', verbose_name='Foto de perfil'),
        ),
    ]