# Generated by Django 2.2.6 on 2020-01-28 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_details_details_visible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='details_visible',
        ),
    ]
