

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
                ('book_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pooled_bn', to='book.Book')),
                ('main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pooled_un', to='accounts.User')),
                ('pooled_user', models.ManyToManyField(related_name='pooled_user', to='accounts.User')),
            ],
        ),
        migrations.CreateModel(
            name='token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('book_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bn', to='book.Book')),
                ('user_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='un', to='accounts.User')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='token',
            unique_together={('user_name', 'book_name')},
        ),
    ]
