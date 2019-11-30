# Generated by Django 2.2.6 on 2019-11-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0030_auto_20191129_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobil',
            name='defect_1_tel',
            field=models.CharField(choices=[('programm', 'Programm'), ('languige', 'Язык'), ('unlock', 'Отвязка'), ('kod', 'Код'), ('akkaunt', 'Аккаунт'), ('lcd/touch', 'LCD/Touch'), ('lcd', 'LCD'), ('touch', 'Touch'), ('не вкл', 'Не вкл'), ('не вкл, мокрый', 'Не вкл, Мокрый'), ('не вкл,падал', 'Не вкл, Падал'), ('not_charging', 'Не заряж'), ('speaker', 'Динамик'), ('buzzer', 'Зуммер'), ('microphone', 'Микрофон'), ('hands_free', 'Hands_Free'), ('wi_fi', 'Wi-Fi'), ('wet', 'Мокрый'), ('sim', 'Sim'), ('flex', 'шлейф'), ('case', 'корпус'), ('------->', '------->')], default='*', max_length=20),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='defect_tel',
            field=models.CharField(choices=[('programm', 'Programm'), ('languige', 'Язык'), ('unlock', 'Отвязка'), ('kod', 'Код'), ('akkaunt', 'Аккаунт'), ('lcd/touch', 'LCD/Touch'), ('lcd', 'LCD'), ('touch', 'Touch'), ('не вкл', 'Не вкл'), ('не вкл, мокрый', 'Не вкл, Мокрый'), ('не вкл,падал', 'Не вкл, Падал'), ('not_charging', 'Не заряж'), ('speaker', 'Динамик'), ('buzzer', 'Зуммер'), ('microphone', 'Микрофон'), ('hands_free', 'Hands_Free'), ('wi_fi', 'Wi-Fi'), ('wet', 'Мокрый'), ('sim', 'Sim'), ('flex', 'шлейф'), ('case', 'корпус'), ('------->', '------->')], max_length=20),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='state',
            field=models.CharField(choices=[('no visible defects', 'Нет видимых дефектов'), ('damaded_LCD/Touch', 'Повреждён экран/тоучскрин'), ('damaded_case', 'Повреждён корпус'), ('damaded_back_cover', 'Повреждена задняя крышка')], max_length=20),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='status',
            field=models.CharField(choices=[('Ремонт', 'ремонт'), ('Рем.завершен', 'ремонт_завершён'), ('Забран', 'забран')], default='Ремонт', max_length=20),
        ),
    ]
