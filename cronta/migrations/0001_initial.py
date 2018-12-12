# Generated by Django 2.1.2 on 2018-12-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailQueue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_to', models.CharField(max_length=200)),
                ('mail_from', models.CharField(default='webmaster@localhost', max_length=200)),
                ('mail_replyto', models.CharField(default=None, max_length=200)),
                ('mail_subject', models.CharField(max_length=200)),
                ('mail_body', models.TextField()),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('sent_datetime', models.DateTimeField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
