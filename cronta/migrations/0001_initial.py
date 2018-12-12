

from django.db import migrations, models
import django.utils.timezone


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
                ('mail_from', models.CharField(default='rehanmallick4080@gmail.com', max_length=200)),
                ('mail_replyto', models.CharField(default='rehanmallick4080@gmail.com', max_length=200)),
                ('mail_subject', models.CharField(max_length=200)),
                ('mail_body', models.TextField()),
                ('scheduled_datetime', models.DateField(default=django.utils.timezone.now, verbose_name='send_time')),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('sent_datetime', models.DateTimeField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
    ]
