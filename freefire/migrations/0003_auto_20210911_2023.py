# Generated by Django 2.1.7 on 2021-09-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freefire', '0002_auto_20210911_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='Matchid',
            field=models.CharField(blank=True, default=138506629933358652, max_length=100, unique=True),
        ),
    ]