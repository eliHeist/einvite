# Generated by Django 4.1.3 on 2023-05-19 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0004_rename_active_guest_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='is_active',
        ),
    ]