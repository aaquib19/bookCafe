# Generated by Django 2.1.2 on 2018-12-11 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cronta', '0005_auto_20181211_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailqueue',
            name='scheduled_datetime',
            field=models.DateField(default=datetime.datetime(2018, 12, 11, 17, 30, 13, 685487, tzinfo=utc), verbose_name='send_time'),
        ),
    ]