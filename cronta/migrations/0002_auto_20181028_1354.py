# Generated by Django 2.1.2 on 2018-10-28 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailqueue',
            name='mail_from',
            field=models.CharField(default='info.educardo@gmail.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='emailqueue',
            name='mail_replyto',
            field=models.CharField(default='info.educardo@gmail.com', max_length=200),
        ),
    ]
