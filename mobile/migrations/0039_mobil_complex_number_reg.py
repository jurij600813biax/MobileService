# Generated by Django 2.2.6 on 2020-02-07 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0038_auto_20200204_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='complex_number_reg',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]