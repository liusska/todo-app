# Generated by Django 3.2 on 2021-08-23 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0008_auto_20210820_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='text',
            new_name='title',
        ),
    ]