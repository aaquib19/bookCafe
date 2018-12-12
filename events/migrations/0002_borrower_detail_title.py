
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrower_detail',
            name='title',
            field=models.BooleanField(default=True),
        ),
    ]
