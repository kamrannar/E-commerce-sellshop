# Generated by Django 4.1.1 on 2022-09-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='city',
            new_name='citys',
        ),
    ]
