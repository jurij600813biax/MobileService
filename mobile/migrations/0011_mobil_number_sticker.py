# Generated by Django 2.2.6 on 2019-11-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0010_auto_20191108_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='number_sticker',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
