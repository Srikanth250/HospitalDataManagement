# Generated by Django 3.0.6 on 2020-05-20 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20200520_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaldetails',
            name='pID',
        ),
    ]
