# Generated by Django 2.2.6 on 2020-01-31 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('send_email', '0006_auto_20200129_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings_common',
            old_name='reg_num_set',
            new_name='contact_number',
        ),
    ]