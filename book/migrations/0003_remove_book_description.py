
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20181212_2011'),

    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]