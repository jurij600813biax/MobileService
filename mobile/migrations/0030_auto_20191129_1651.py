# Generated by Django 2.2.6 on 2019-11-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0029_auto_20191129_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobil',
            name='model_tel',
            field=models.CharField(choices=[('IPhone', 'IPhone'), ('Samsung', 'Samsung'), ('Huawei', 'Huawei'), ('Meizu', 'Meizu'), ('Xiaomi', 'Xiaomi'), ('Nokia', 'Nokia'), ('Microsoft', 'Microsoft'), ('Prestigio', 'Prestigio'), ('Sony', 'Sony'), ('Alkatel', 'Alcatel'), ('Asus', 'Asus'), ('Aser', 'Aser'), ('Amigo', 'Amigo'), ('Amoi', 'Amoi'), ('BlackView', 'BlackView'), ('BLU', 'BLU'), ('BQ', 'BQ'), ('BlackBerry', 'BlackBerry'), ('CAT', 'CAT'), ('Caterpillar', 'Caterpillar'), ('Coolpad', 'Coolpad'), ('Cubot', 'Cubot'), ('Doogee', 'Doogee'), ('Doro', 'Doro'), ('Elephone', 'Elephone'), ('Estar', 'Estar'), ('Gigabyte', 'Gigabyte'), ('Getnord', 'Getnord'), ('Google', 'Google'), ('HTC', 'HTC'), ('HomTom', 'HomTom'), ('HP', 'HP'), ('Kazam', 'Kazam'), ('Lenovo', 'Lenovo'), ('LG', 'Lg'), ('MyPhone', 'MyPhone'), ('Nous', 'Nous'), ('OnePlus', 'OnePlus'), ('Oukitel', 'Oukitel'), ('Zopo', 'Zopo'), ('ZTE', 'ZTE'), ('------->', '------->')], max_length=20),
        ),
    ]