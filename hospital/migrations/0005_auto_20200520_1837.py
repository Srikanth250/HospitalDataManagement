# Generated by Django 3.0.6 on 2020-05-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20200520_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalhistory',
            name='pname',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='medical', to='hospital.GeneralDetails'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='drugList',
            field=models.TextField(),
        ),
    ]
