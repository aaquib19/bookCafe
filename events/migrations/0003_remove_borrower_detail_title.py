
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_borrower_detail_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower_detail',
            name='title',
        ),
    ]