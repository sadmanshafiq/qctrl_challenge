# Generated by Django 3.0 on 2019-12-24 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0004_auto_20191223_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controls',
            name='ctype',
            field=models.CharField(choices=[('Gaussian', 'Gaussian'), ('Primitive', 'Primitive'), ('CORPSE', 'CORPSE'), ('CinBB', 'CinBB'), ('CinSK', 'CinSK')], default='CinBB', max_length=10),
        ),
    ]
