# Generated by Django 3.0.6 on 2020-05-20 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_generaldetails_pid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generaldetails',
            name='pId',
        ),
    ]
