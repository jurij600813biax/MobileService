# Generated by Django 2.2.6 on 2020-01-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20200105_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='detail_visible',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
