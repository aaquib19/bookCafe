# Generated by Django 2.1.2 on 2018-12-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('emaild', models.EmailField(max_length=255)),
                ('bookname', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
