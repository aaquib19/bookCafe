# Generated by Django 2.1.2 on 2018-12-12 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181212_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower_detail',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User'),
        ),
    ]
