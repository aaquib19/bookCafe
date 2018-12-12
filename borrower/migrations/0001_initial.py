

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pooled_token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pooled_bn', to='book.Book')),
                ('main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pooled_token', to='accounts.User')),
                ('pooled_user', models.ManyToManyField(related_name='pooled_user', to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField(unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rdate', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='book.Book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.User')),
                ('user2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='accounts.User')),
                ('user3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user3', to='accounts.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='token',
            unique_together={('user', 'book')},
        ),
    ]
