# Generated by Django 2.2.6 on 2019-11-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0027_auto_20191124_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobil',
            name='defect_1_tel',
            field=models.CharField(choices=[('programm', 'Programm'), ('kod', 'Код'), ('akkaunt', 'Аккаунт'), ('lcd/touch', 'LCD/Touch'), ('lcd', 'LCD'), ('touch', 'Touch'), ('не вкл', 'Не вкл'), ('не вкл, мокрый', 'Не вкл, Мокрый'), ('не вкл,падал', 'Не вкл, Падал'), ('not_charging', 'Не заряж'), ('speaker', 'Speaker'), ('buzzer', 'Buzzer'), ('microphone', 'Microphone'), ('hands_free', 'Hands_Free'), ('wi_fi', 'Wi-Fi'), ('wet', 'Мокрый'), ('sim', 'Sim'), ('------->', '------->')], default='*', max_length=20),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='defect_tel',
            field=models.CharField(choices=[('programm', 'Programm'), ('kod', 'Код'), ('akkaunt', 'Аккаунт'), ('lcd/touch', 'LCD/Touch'), ('lcd', 'LCD'), ('touch', 'Touch'), ('не вкл', 'Не вкл'), ('не вкл, мокрый', 'Не вкл, Мокрый'), ('не вкл,падал', 'Не вкл, Падал'), ('not_charging', 'Не заряж'), ('speaker', 'Speaker'), ('buzzer', 'Buzzer'), ('microphone', 'Microphone'), ('hands_free', 'Hands_Free'), ('wi_fi', 'Wi-Fi'), ('wet', 'Мокрый'), ('sim', 'Sim'), ('------->', '------->')], max_length=20),
        ),
    ]
