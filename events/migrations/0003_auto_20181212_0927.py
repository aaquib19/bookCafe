# Generated by Django 2.1.2 on 2018-12-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181212_0924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrower_detail',
            options={},
        ),
        migrations.AddField(
            model_name='borrower_detail',
            name='title',
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
    ]
