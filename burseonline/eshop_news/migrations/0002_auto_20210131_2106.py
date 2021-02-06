# Generated by Django 3.1.5 on 2021-01-31 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 31, 21, 6, 52, 151321), null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='pub_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 31, 21, 6, 52, 151321), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 31, 21, 6, 52, 150322), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 31, 21, 6, 52, 150322), null=True),
        ),
    ]
