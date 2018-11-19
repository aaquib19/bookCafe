
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unread', models.BooleanField(db_index=True, default=True)),
                ('notification_title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('emailed', models.BooleanField(db_index=True, default=False)),
                ('description_view', models.BooleanField(db_index=True, default=False)),
                ('recipient', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='accounts.User')),
            ],
        ),
    ]
