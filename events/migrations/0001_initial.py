

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('accounts', '0001_initial'),

        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrower_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateField()),
                ('returning_date', models.DateField(blank=True, null=True)),
                ('submission_date', models.DateField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=False)),
                ('fine', models.IntegerField(blank=True, null=True)),
                ('book_name', models.ManyToManyField(to='book.Book')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
                ('pooled_users', models.ManyToManyField(blank=True, null=True, related_name='book_pooling_users', to='accounts.User')),
            ],
            options={
                'verbose_name': 'Scheduling',
                'verbose_name_plural': 'Scheduling',
            },
        ),
    ]
