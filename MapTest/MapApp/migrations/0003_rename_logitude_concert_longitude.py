# Generated by Django 4.0.4 on 2022-06-01 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MapApp', '0002_alter_concert_latitude_alter_concert_logitude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='concert',
            old_name='logitude',
            new_name='longitude',
        ),
    ]
