# Generated by Django 3.0.3 on 2020-02-27 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200226_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='default.png', upload_to='profile_image/%d/%m/%Y', verbose_name='Foto de perfil'),
        ),
    ]
