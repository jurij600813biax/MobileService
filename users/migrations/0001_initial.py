# Generated by Django 2.2.6 on 2019-12-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_model', models.CharField(max_length=20)),
                ('LCD_orig', models.CharField(max_length=6)),
                ('LCD_HQ', models.CharField(max_length=6)),
                ('charging', models.CharField(max_length=6)),
                ('record_1', models.CharField(max_length=20)),
                ('record_2', models.CharField(max_length=20)),
                ('record_3', models.CharField(max_length=20)),
            ],
        ),
    ]
