# Generated by Django 2.1.2 on 2018-12-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_remove_borrower_detail_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower_detail',
            name='title',
            field=models.CharField(blank=True, max_length=123, null=True),
        ),
    ]
