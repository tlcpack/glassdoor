# Generated by Django 3.1.1 on 2020-09-29 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200928_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='content',
        ),
    ]
