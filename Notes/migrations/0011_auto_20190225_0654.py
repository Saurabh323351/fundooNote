# Generated by Django 2.1.5 on 2019-02-25 06:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0010_auto_20190225_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='is_archived',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='notes',
            name='reminder',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 6, 54, 28, 6985, tzinfo=utc), null=True),
        ),
    ]