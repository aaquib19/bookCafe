# Generated by Django 2.1.2 on 2018-12-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_emailactivation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_no',
            field=models.IntegerField(blank=True, max_length=10, null=True),
        ),
    ]