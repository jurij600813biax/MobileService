# Generated by Django 2.2.6 on 2020-02-26 17:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0010_auto_20200208_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='send_message',
            name='send_message_performance',
        ),
        migrations.AddField(
            model_name='send_message',
            name='send_message_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
