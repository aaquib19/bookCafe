# Generated by Django 2.1.2 on 2018-12-08 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrower', '0006_token_rdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='rdate',
            field=models.DateTimeField(),
        ),
    ]
