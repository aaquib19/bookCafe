# Generated by Django 2.1.2 on 2018-12-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_merge_20181212_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
