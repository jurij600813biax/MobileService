# Generated by Django 2.2.6 on 2020-01-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0005_auto_20200128_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings_common',
            name='free_set',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20),
        ),
    ]
