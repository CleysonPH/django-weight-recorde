# Generated by Django 3.0.3 on 2020-02-26 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(blank=True, null=True, verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/%d/%m/%Y', verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight_goal',
            field=models.FloatField(blank=True, null=True, verbose_name='Meta de peso'),
        ),
    ]
