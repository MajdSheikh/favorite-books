# Generated by Django 4.1.1 on 2022-10-02 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='User',
        ),
    ]