

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrower_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_id', models.CharField(blank=True, max_length=123, null=True)),
                ('issue_date', models.DateField()),
                ('returning_date', models.DateField(blank=True, null=True)),
                ('submission_date', models.DateField()),
                ('deleted', models.BooleanField(default=False)),
                ('book_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
                ('pooled_users', models.ManyToManyField(related_name='book_pooling_users', to='accounts.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='borrower_detail',
            unique_together={('name', 'book_name')},
        ),
    ]
