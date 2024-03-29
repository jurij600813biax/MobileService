# Generated by Django 2.2.6 on 2019-11-07 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0008_auto_20191103_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='model_1_tel',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mobil',
            name='price',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mobil',
            name='model_tel',
            field=models.CharField(choices=[('samsung', 'Samsung'), ('sony', 'Sony'), ('nokia', 'Nokia'), ('apple', 'Apple'), ('asus', 'Asus'), ('huawei', 'Huawei'), ('lenovo', 'Lenovo'), ('lg', 'Lg'), ('meizu', 'Meizu'), ('xiaomi', 'Xiaomi'), ('microsoft', 'Microsoft'), ('Other', 'Other')], max_length=50),
        ),
    ]
