# Generated by Django 2.1.2 on 2018-12-11 17:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cronta', '0007_auto_20181211_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailqueue',
            name='scheduled_datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 11, 17, 32, 38, 819467, tzinfo=utc), verbose_name='send_time'),
        ),
    ]