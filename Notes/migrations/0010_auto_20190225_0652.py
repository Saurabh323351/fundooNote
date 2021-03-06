# Generated by Django 2.1.5 on 2019-02-25 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0009_auto_20190223_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='note_images/'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='reminder',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 25, 6, 52, 37, 815754, tzinfo=utc), null=True),
        ),
    ]
