# Generated by Django 2.1.2 on 2018-12-12 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181212_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower_detail',
            name='title',
        ),
    ]