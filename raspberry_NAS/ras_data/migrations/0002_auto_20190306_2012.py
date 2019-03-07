# Generated by Django 2.1.7 on 2019-03-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ras_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ras_info',
            name='data',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='ras_info',
            name='cpu_temperature',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ras_info',
            name='cpu_useage',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ras_info',
            name='harddrive_useage',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ras_info',
            name='humidity',
            field=models.FloatField(max_length=255),
        ),
        migrations.AlterField(
            model_name='ras_info',
            name='temperature',
            field=models.FloatField(max_length=255),
        ),
    ]
