# Generated by Django 2.2.6 on 2020-01-20 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20200120_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='detail_visible',
            field=models.CharField(choices=[('Видимый', 'Видимый'), ('Невидимый', 'Невидимый')], max_length=10),
        ),
    ]
