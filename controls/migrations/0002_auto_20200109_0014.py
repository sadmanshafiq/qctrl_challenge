# Generated by Django 3.0 on 2020-01-09 00:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controls',
            old_name='ctype',
            new_name='type',
        ),
    ]
