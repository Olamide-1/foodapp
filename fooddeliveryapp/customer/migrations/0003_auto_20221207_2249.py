# Generated by Django 2.1.1 on 2022-12-07 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20221207_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='phone_num',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='ordermodel',
            old_name='postal_code',
            new_name='number',
        ),
    ]
