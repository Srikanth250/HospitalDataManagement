# Generated by Django 3.0.6 on 2020-05-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_remove_generaldetails_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generaldetails',
            name='pFname',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
